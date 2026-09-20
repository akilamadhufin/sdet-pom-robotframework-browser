from Libraries.UIClient import UIClient

class Actions:

    LOGOUT_BUTTON = "//a[@href='/logout' and contains(text(),'Logout')]"
    LOGIN_EMAIL_INPUT = "//input[@data-qa='login-email']"
    LOGIN_PASSOWRD_INPUT = "//input[@data-qa='login-password']"
    LOGIN_BUTTON = "//button[@data-qa='login-button']" 
    LOGGED_USER_NAME = "//li/a/b[text()='REPLACE_ME']"
    DELETE_ACCOUNT_BUTTON = "//a[contains(text(),'Delete Account')]"
    ACCOUNT_DELETED_MESSAGE = "//h2[@data-qa='account-deleted']"
    CONTINUE_BUTTON = "//a[@data-qa='continue-button']"

    def __init__(self, client: UIClient):
        self.client = client

    def click_logout(self):
        self.client.click_w(self.LOGOUT_BUTTON)

    def enter_login_email(self,email):
        self.client.type_text(self.LOGIN_EMAIL_INPUT, email)

    def enter_login_password(self,password):
        self.client.type_text(self.LOGIN_PASSOWRD_INPUT, password)

    def click_login_button(self):
        self.client.click_w(self.LOGIN_BUTTON)
        self.client.wait_until_page_idle()

    def verify_user_login(self, name):
        self.client.wait_for_element_to_be_visible(self.LOGGED_USER_NAME.replace("REPLACE_ME", name))    

    def click_delete_account(self):
        self.client.click_w(self.DELETE_ACCOUNT_BUTTON)

    def wait_for_account_deleted(self):
        self.client.wait_for_element_to_be_visible(self.ACCOUNT_DELETED_MESSAGE)  

    def click_continue_after_delete(self):
        self.client.click_w(self.CONTINUE_BUTTON)

    def wait_username_hidden_after_delete(self, name):
        locator = self.LOGGED_USER_NAME.replace("REPLACE_ME", name)
        self.client.wait_hidden(locator)   

class Tasks:

    """
    High-level workflow layer for login.
    This is what CTX.login will call.
    """

    def __init__(self, client: UIClient):
        self.actions = Actions(client)

    def click_logout(self):
        self.actions.click_logout()

    def user_login(self, email, password):
        self.actions.enter_login_email(email)                   
        self.actions.enter_login_password(password)
        self.actions.click_login_button()

    def verify_user_login_correctly(self, name):
        self.actions.verify_user_login(name)


    def delete_account_and_verify(self, name):
        self.actions.click_delete_account()
        self.actions.wait_for_account_deleted()
        self.actions.click_continue_after_delete()
        self.actions.wait_username_hidden_after_delete(name)                