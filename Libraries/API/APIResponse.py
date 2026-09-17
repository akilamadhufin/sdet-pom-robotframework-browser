class APIResponse:
    """
    Wraps the raw HTTP response and provides safe access
    to status, text, JSON, and helper methods.
    """

    def __init__(self, response):
        self._response = response # Store the original raw HTTP response object.
        self.status_code = response.status_code # The numeric HTTP status code (e.g., 200, 404, 500).
        self.reason = response.reason # Short text describing the status (e.g., "OK", "Not Found").
        self.headers = response.headers # All HTTP response headers returned by the server.
        self.text = response.text # The raw response body as a string.
        self.is_success = response.ok # True if status code is 200–399, otherwise False.

        try:
            self.json = response.json() # Parsed JSON body (converted into a Python dict).

        except ValueError:
            self.json = None

    def get_value(self, key: str):
        # Return exactly one value for the given key.
        values = self.get_values(key)
        if len(values) != 1:
            raise ValueError(f"Expected one value for {key}, but got {len(values)}")
        return values[0]

    def get_values(self, key: str):
        # Return a list of value (one value) for the given key.
        if isinstance(self.json, dict) and key in self.json: 
            # checks whether the response json is a dictionary ? 
            # does it contain the key that we are looking for ?
            return [self.json[key]] # if both are true, return the value inside a list
        return []

    def __repr__(self):
        """
        Developer-friendly string representation of the response object.
        Useful for logging, debugging, and console output.
        """
        return f"APIResponse(status_code={self.status_code})"