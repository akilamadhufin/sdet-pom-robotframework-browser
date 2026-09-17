from Browser import Browser
from Browser.utils.data_types import SupportedBrowsers, ElementState, SelectAttribute
from datetime import timedelta

class UIClient:

    def __init__(self, url, headless=False):
        """
        Initialize Playwright (via Browser library), open a browser, create a context,
        and navigate to the starting URL.
        """

        # Create Browser engine-(timeouts, retries, logging)
        self.browser = Browser(
            timeout=timedelta(seconds=30), # Stop action if it takes more than 30s
            retry_assertions_for=timedelta(seconds=5), # If a check fails, retry for 5s
            show_keyword_call_banner=True # Show Robot Framework logs
        )

        # Open a Chromium browser
        self.browser.new_browser(
            browser=SupportedBrowsers.chromium, # Use Chromium browser
            headless=headless, # True = no UI, False = show UI
            slowMo=timedelta(milliseconds=100) # slowdown each browser action by 100ms. It gives time to loads pages and views
        )

        # Creating a fresh browser session- Without a context, cookies, storage, and sessions leak between tests.
        self.browser.new_context(ignoreHTTPSErrors=True)

        # Open the first page of the test. Place where 1st test starts
        self.browser.new_page(url)


    # ---------------------------------------------------------
    # Basic UI Actions
    # ---------------------------------------------------------

    # Custom click
    def click_w(self, selector):
        self.browser.click(selector=selector)

    def type_text(self, selector, text):
        self.browser.type_text(selector=selector, txt=text)

    def fill_text(self, selector, text):
        self.browser.fill_text(selector=selector, txt=text)

    def clear_text(self, selector):
        self.browser.clear_text(selector=selector)

    def select_option(self, selector, value):
        self.browser.select_options_by(selector, SelectAttribute.value, value)

    # ---------------------------------------------------------
    # WAIT FUNCTIONS
    # ---------------------------------------------------------

    def wait_for_element_to_be_visible(self, selecctor, timeout="5 s"):
        self.browser.wait_for_elements_state(selector=selecctor, state=ElementState.visible, timeout=timeout)


    def wait_hidden(self, selector, timeout="5 s"):
        self.browser.wait_for_elements_state(selector=selector, state=ElementState.hidden, timeout=timeout)


    # ---------------------------------------------------------
    # GETTERS
    # ---------------------------------------------------------
    # Needed for validations (checking messages, labels, etc.)
    def get_text(self, selector):
        return self.browser.get_text(selector=selector)

    def get_count(self, selector):
        return self.browser.get_element_count(selector=selector)


    # ---------------------------------------------------------
    # PAGE IDLE
    # ---------------------------------------------------------

    def wait_until_page_idle(self, timeout="5 s"):
        self.browser.wait_for_load_state("domcontentloaded", timeout=timeout)

    # ---------------------------------------------------------
    # CLOSE BROWSER
    # ---------------------------------------------------------      

    def close_browser(self):
        try:
            self.browser.close_browser("ALL")

        except Exception:
            pass    
