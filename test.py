# File: Libraries/Views/MainView.py

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
    HOME_BUTTON = "//a[contains(text(),'Home')]"
    SIGNUP_LOGIN_BUTTON = "//a[contains(text(),'Signup / Login')]"
    PRODUCTS_BUTTON = "//a[contains(text(),'Products')]"
    CART_BUTTON = "//a[contains(text(),'Cart')]"
    CONTACT_US_BUTTON = "//a[contains(text(),'Contact us')]"
    TEST_CASES_BUTTON = "//a[contains(text(),'Test Cases')]"
    API_TESTING_BUTTON = "//a[contains(text(),'API Testing')]"
    VIDEO_TUTORIALS_BUTTON = "//a[contains(text(),'Video Tutorials')]"

    # Placeholder loading spinner (AutomationExercise has none)
    LOADING_SPINNER = "//div[@id='loading']"

    def __init__(self, client):
        self.client = client

    # -----------------------------------------
    # GLOBAL WAIT HELPERS
    # -----------------------------------------
    def wait_until_page_is_idle(self):
        """Wait for DOM and network stability."""
        self.client.wait_for_dom_stable()
        self.client.wait_for_network_idle()

    def wait_for_loading_to_finish(self):
        """Wait for loading spinner if present."""
        self.client.wait_for_element_to_be_hidden(
            self.LOADING_SPINNER, timeout="5 s"
        )

    # -----------------------------------------
    # GLOBAL NAVIGATION ACTIONS
    # -----------------------------------------
    def go_home(self):
        self.client.click_w(self.HOME_BUTTON)
        self.wait_until_page_is_idle()

    def go_signup_login(self):
        self.client.click_w(self.SIGNUP_LOGIN_BUTTON)
        self.wait_until_page_is_idle()

    def go_products(self):
        self.client.click_w(self.PRODUCTS_BUTTON)
        self.wait_until_page_is_idle()

    def go_cart(self):
        self.client.click_w(self.CART_BUTTON)
        self.wait_until_page_is_idle()

    def go_contact_us(self):
        self.client.click_w(self.CONTACT_US_BUTTON)
        self.wait_until_page_is_idle()

    def go_test_cases(self):
        self.client.click_w(self.TEST_CASES_BUTTON)
        self.wait_until_page_is_idle()

    def go_api_testing(self):
        self.client.click_w(self.API_TESTING_BUTTON)
        self.wait_until_page_is_idle()

    def go_video_tutorials(self):
        self.client.click_w(self.VIDEO_TUTORIALS_BUTTON)
        self.wait_until_page_is_idle()
