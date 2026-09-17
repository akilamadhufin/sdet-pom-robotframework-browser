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
        self.base_url = base_url.rstrip("/") # Remove trailing slash if user adds it
        self.timeout = timeout
        self.session = None

    def connect(self):
        """Create a reusable HTTP session."""
        self.session = requests.Session()
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
    
                                