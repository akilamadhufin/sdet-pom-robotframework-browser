class MainView:
    """
    Global navigation controller for the AutomationExercise website.

    This class defines all top-level navigation elements and provides
    reusable methods for moving between major sections of the site.
    It also centralizes page-idle and loading-wait logic so that
    every navigation action begins and ends in a stable UI state.
    """

    # -----------------------------------------
    # GLOBAL NAVIGATION LOCATORS
    # -----------------------------------------

    HOME_BUTTON = "//a[@href='/' and contains(text(),'Home')]"
    SIGNUP_LOGIN_BUTTON = "//a[@href='/login' and contains(text(),'Signup / Login')]"
    PRODUCTS_BUTTON = "//a[contains(text(),'Products')]"
    CART_BUTTON = "//a[contains(text(),'Cart')]"
    CONTACT_US_BUTTON = "//a[contains(text(),'Contact us')]"
    TEST_CASES_BUTTON = "//a[contains(text(),'Test Cases')]"
    API_TESTING_BUTTON = "//a[contains(text(),'API Testing')]"
    VIDEO_TUTORIALS_BUTTON = "//a[contains(text(),'Video Tutorials')]"

    LOADING_SPINNER = "//div[@id='loading']"

    def __init__(self, client):
        """
        Store the UIClient instance so this view can perform clicks,
        waits, and navigation using the browser engine.
        """
        self.client = client # This the oject create from UICLient.py

    # -----------------------------------------
    # GLOBAL WAIT HELPERS
    # -----------------------------------------
    def wait_until_page_is_idle(self):
        """
        Wait until the page is stable:
        - DOM is not changing
        - Network requests are finished
        """
        self.client.wait_until_page_idle()


    def wait_for_loading_to_finish(self):
        """
        Wait until the loading spinner disappears.
        (AutomationExercise normally has no spinner, but this keeps
        the structure consistent.)
        """
        self.client.wait_hidden(self.LOADING_SPINNER, timeout="5 s")


    # -----------------------------------------
    # GLOBAL NAVIGATION ACTIONS
    # ----------------------------------------- 
    def go_home(self):
        """Navigate to the Home page."""
        self.client.click_w(self.HOME_BUTTON)
        self.wait_until_page_is_idle() 

    def go_signup_login(self):
        """Navigate to the Signup/Login page."""        
        self.client.click_w(self.SIGNUP_LOGIN_BUTTON)
        self.wait_until_page_is_idle()

    def go_products(self):
        """Navigate to the Products page."""
        self.client.click_w(self.PRODUCTS_BUTTON)
        self.wait_until_page_is_idle()

    def go_cart(self):
        """Navigate to the Cart page."""
        self.client.click_w(self.CART_BUTTON)
        self.wait_until_page_is_idle()

    def go_contact_us(self):
        """Navigate to the Contact Us page."""
        self.client.click_w(self.CONTACT_US_BUTTON)
        self.wait_until_page_is_idle()

    def go_test_cases(self):
        """Navigate to the Test Cases page."""
        self.client.click_w(self.TEST_CASES_BUTTON)
        self.wait_until_page_is_idle()

    def go_api_testing(self):
        """Navigate to the API Testing page."""
        self.client.click_w(self.API_TESTING_BUTTON)
        self.wait_until_page_is_idle()

    def go_video_tutorials(self):
        """Navigate to the Video Tutorials page."""
        self.client.click_w(self.VIDEO_TUTORIALS_BUTTON)
        self.wait_until_page_is_idle()     
