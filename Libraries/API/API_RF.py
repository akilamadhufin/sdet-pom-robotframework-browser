# UserApi_RF.py
# ---------------------------------------------------------
# Robot Framework Library Entry Point
# Loads:
#   - APIClient
#   - APIEndpoints
#   - APITasks
# Exposes all decorated keywords to Robot Framework
# ---------------------------------------------------------

from robotlibcore import DynamicCore
from Libraries.API.APIClient import APIClient
from Libraries.API.APIEndpoints import APIEndpoints
from Libraries.API.APITasks import APITasks

class API_RF(DynamicCore):
    """
    Robot Framework library that exposes APIEndpoints and APITasks
    as Robot Framework keywords.
    """

    def __init__(self, base_url: str):

        # Create the HTTP client
        client = APIClient(base_url)

        # Load both layers into Robot Framework
        super().__init__([
            APIEndpoints(client),
            APITasks(client)
        ])