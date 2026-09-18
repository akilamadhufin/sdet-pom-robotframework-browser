# This file responsible for
# building the base URL
# sending HTTP requests
# returning APIResponse
# raising errors if something goes wrong

import requests
from Libraries.API.APIErrors import RequestError, NotConnectedError
from Libraries.API.APIResponse import APIResponse

class APIClient:
    """
    Enterprise-level API client.
    - Uses a persistent session (faster, reusable)
    - Uses a single internal _request() method
    - Supports GET, POST, DELETE, PUT
    - Uses dependency injection for base_url
    - Uses timeout
    """

    def __init__(self, base_url: str, timeout: int=30):
        base_url = base_url.rstrip("/")
        if base_url.endswith("/api"):
            self.base_url = base_url
            self.site_url = base_url[:-4]
        else:
            self.site_url = base_url
            self.base_url = f"{base_url}/api"
        self.timeout = timeout
        self.session = None

    def connect(self):
        """    
        Create a reusable HTTP session and initialize the CSRF data required
        by Automation Exercise for unsafe requests such as DELETE.
        """
        self.session = requests.Session()

        # Django checks that unsafe HTTPS requests come from the same site.
        self.session.headers.update({
            "Accept": "application/json, text/plain, */*",
            "Origin": self.site_url,
            "Referer": f"{self.site_url}/",
            "User-Agent": "Basic-SWT API Test Client"
        })

        try:
            # Visit a page that supplies the CSRF cookie.
            self.session.get(
                f"{self.site_url}/login",
                timeout=self.timeout
            ).raise_for_status()

            # Send the CSRF token as a header on DELETE/POST/PUT requests.
            csrf_token = self.session.cookies.get("csrftoken")
            if csrf_token:
                self.session.headers.update({
                    "X-CSRFToken": csrf_token
                })

        except requests.RequestException as error:
            raise RequestError(f"Could not initialize API session. {error}") from error        

        return self

    def _request(self, method: str, endpoint: str, payload: dict | None = None, params: dict | None = None):
        """
        Core request handler.
        All HTTP methods (GET, POST, DELETE, PUT) go through here.
        """ 

        if self.session is None:
            raise NotConnectedError("API client is not connected")

        url = f"{self.base_url}/{endpoint.lstrip('/')}" # safe join

        try:
            response = self.session.request(
                method=method,
                url=url,
                data=payload, # AutomationExercise API uses form-data
                params=params, # GET parameters
                timeout=self.timeout
            )

        except requests.RequestException as error:
            raise RequestError(f"API request failed: {error}") from error

        return APIResponse(response)

    # Public methods

    def get(self, endpoint: str, params: dict | None = None) -> APIResponse:
        return self._request("GET", endpoint, params=params)

    def post(self, endpoint: str, payload: dict | None = None) -> APIResponse:
        return self._request("POST", endpoint, payload=payload)

    def delete(self, endpoint: str, payload: dict | None = None) -> APIResponse: 
        return self._request("DELETE", endpoint, payload=payload)

    def put(self, endpoint: str, payload: dict | None = None) -> APIResponse:
        return self._request("PUT", endpoint, payload=payload)


    def close_session(self):
        """Close the session."""
        if self.session is not None:
            self.session.close()
            self.session = None
    
                                