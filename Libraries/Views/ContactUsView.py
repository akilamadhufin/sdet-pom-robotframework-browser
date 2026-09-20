from Libraries.UIClient import UIClient

class Actions:

    NAME_INPUT = "//input[@data-qa='name']"
    EMAIL_INPUT = "//input[@data-qa='email']"
    SUBJECT_INPUT = "//input[@data-qa='subject']"
    MESSAGE_TEXTAREA = "//textarea[@data-qa='message']"
    UPLOAD_INPUT = "//input[@name='upload_file']"
    SUBMIT_BUTTON = "//input[@data-qa='submit-button']"
    SUCCESS_MESSAGE = "//div[@class='status alert alert-success']"
    HOME_BUTTON = "//a[@class='btn-success']"

    def __init__(self, client: UIClient):
        self.client = client

    def fill_form(self, name, email, subject, message):
        self.client.type_text(self.NAME_INPUT, name)
        self.client.type_text(self.EMAIL_INPUT, email)
        self.client.type_text(self.SUBJECT_INPUT, subject)
        self.client.type_text(self.MESSAGE_TEXTAREA, message) 

    def upload_file(self, file_path):
        self.client.upload_file(self.UPLOAD_INPUT, file_path)

    def submit_form(self):
        self.client.click_w(self.SUBMIT_BUTTON)
        self.client.sleep(10)   
        # self.client.wait_until_page_idle()
        # self.client.accept_alert()
        
    def wait_for_success(self):
        self.client.wait_for_element_to_be_visible(self.SUCCESS_MESSAGE)

    def click_Home(self):
        self.client.click_w(self.HOME_BUTTON)
        self.client.wait_until_page_idle()

class Tasks:

    def __init__(self, client: UIClient):
        self.actions = Actions(client)

    def submit_contact_us_form(self, name, email, subject, message, file_path):
        self.actions.fill_form(name, email, subject, message)
        self.actions.upload_file(file_path)
        self.actions.submit_form()
        # self.actions.wait_for_success()
        # self.actions.click_Home()                                     