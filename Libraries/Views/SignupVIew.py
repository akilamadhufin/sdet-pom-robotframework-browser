from Libraries.UIClient import UIClient

class Actions:

    NAME_INPUT = "//input[@data-qa='signup-name']"
    EMAIL_INPUT = "//input[@data-qa='signup-email']"
    SIGNUP_BUTTON = "//button[@data-qa='signup-button']"

    TITLE_RADIO_MR = "//input[@id='id_gender1']"
    TITLE_RADIO_MRS = "//input[@id='id_gender2']"

    PASSWORD_INPUT = "//input[@id='password']"

    DAY_DROPDOWN = "//select[@id='days']"
    MONTH_DROPDOWN = "//select[@id='months']"
    YEAR_DROPDOWN = "//select[@id='years']"

    NEWSLETTER_CHECKBOX = "//input[@id='newsletter']"
    OFFERS_CHECKBOX = "//input[@id='optin']"

    FIRST_NAME = "//input[@id='first_name']"
    LAST_NAME = "//input[@id='last_name']"
    COMPANY = "//input[@id='company']"
    ADDRESS1 = "//input[@id='address1']"
    ADDRESS2 = "//input[@id='address2']"
    COUNTRY = "//select[@id='country']"
    STATE = "//input[@id='state']"
    CITY = "//input[@id='city']"
    ZIPCODE = "//input[@id='zipcode']"
    MOBILE_NUMBER = "//input[@id='mobile_number']"

    CREATE_ACCOUNT_BUTTON = "//button[@data-qa='create-account']"

    def __init__(self, client: UIClient):
        self.client = client

    # -----------------------------
    # LOW-LEVEL ACTIONS
    # -----------------------------

    def enter_name(self, name):
        self.client.type_text(self.NAME_INPUT, name)    

    def enter_email(self, email):
        self.client.type_text(self.EMAIL_INPUT, email)

    def click_signup(self):
        self.client.click_w(self.SIGNUP_BUTTON)

    def select_title_mr(self):
        self.client.click_w(self.TITLE_RADIO_MR)    

    def select_title_mrs(self):
        self.client.click_w(self.TITLE_RADIO_MRS)     

    def enter_password(self, password):
        self.client.type_text(self.PASSWORD_INPUT, password)

    def select_day(self, day):
        self.client.select_option(self.DAY_DROPDOWN, day) 

    def select_month(self, month):
        self.client.select_option(self.MONTH_DROPDOWN, month)

    def select_year(self, year):
        self.client.select_option(self.YEAR_DROPDOWN, year)

    def toggle_newsletter(self):
        self.client.click_w(self.NEWSLETTER_CHECKBOX)  

    def toggle_offers(self):
        self.client.click_w(self.OFFERS_CHECKBOX)          

    def enter_first_name(self, first_name):
        self.client.type_text(self.FIRST_NAME, first_name)    

    def enter_last_name(self, last_name):
        self.client.type_text(self.LAST_NAME, last_name)

    def enter_company(self, company):
        self.client.type_text(self.COMPANY, company)

    def enter_address1(self, address):
        self.client.type_text(self.ADDRESS1, address)

    def enter_address2(self, address):
        self.client.type_text(self.ADDRESS2, address)        

    def select_country(self, country):
        self.client.select_option(self.COUNTRY, country)

    def enter_state(self, state):
        self.client.type_text(self.STATE, state)

    def enter_city(self, city):
        self.client.type_text(self.CITY, city)

    def enter_zipcode(self, zipcode):
        self.client.type_text(self.ZIPCODE, zipcode)

    def enter_mobile(self, mobile):
        self.client.type_text(self.MOBILE_NUMBER, mobile)

    def click_create_account(self):
        self.client.click_w(self.CREATE_ACCOUNT_BUTTON)


class Tasks:
    """
    High-level workflow layer for Signup.
    This is what CTX.signup will call.
    """

    def __init__(self, client: UIClient):
        self.actions = Actions(client)

    def register_user(self,name, email, password, day, month, year, first_name, last_name, company, address1, address2, country, state, city, zipcode, mobile):
        # 1–3: signup name/email/button
        self.actions.enter_name(name)  
        self.actions.enter_email(email)
        self.actions.click_signup()

        # 4–5: title + password
        self.actions.select_title_mr()
        self.actions.enter_password(password)

        # 6–8: date of birth
        self.actions.select_day(day)
        self.actions.select_month(month)
        self.actions.select_year(year)

        # 9–10: newsletter + offers
        self.actions.toggle_newsletter()
        self.actions.toggle_offers()

        # 11–18: address + contact
        self.actions.enter_first_name(first_name)
        self.actions.enter_last_name(last_name)
        self.actions.enter_company(company)
        self.actions.enter_address1(address1)
        self.actions.enter_address2(address2)
        self.actions.select_country(country)
        self.actions.enter_state(state)
        self.actions.enter_city(city)
        self.actions.enter_zipcode(zipcode)
        self.actions.enter_mobile(mobile)

        # 19: create account
        self.actions.click_create_account()      