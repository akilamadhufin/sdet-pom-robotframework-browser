# Basic API error types used across the API layer.

class APIErrors(Exception): #Create a new error type called ApiError that behaves like any normal Python error
    # Base class for all API-related errors.
    pass

class NotConnectedError(APIErrors):
    # Raised when the API client is used before connecting. 
    pass

class ResponseValueError(APIErrors):
    # Raised when expected JSON fields are missing or invalid.
    pass

class RequestError(APIErrors):
    # Raised when an API request returns an unsuccessful status code.
    pass
