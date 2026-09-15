from Libraries.UIClient import UIClient

class Actions:

    LOGOUT_BUTTON = "//a[@href='/logout' and contains(text(),'Logout')]"

    def __init__(self, client: UIClient):
        self.client = client

    def click_logout(self):
        self.client.click_w(self.LOGOUT_BUTTON)


class Tasks:

    """
    High-level workflow layer for login.
    This is what CTX.login will call.
    """

    def __init__(self, client: UIClient):
        self.actions = Actions(client)

    def click_logout(self):
        self.actions.click_logout()               
