from Libraries.ContextHolder import CTX
from Libraries.UIClient import UIClient
from Libraries.UILibrary.MainTasks import MainTasks
from Libraries.Views.SignupView import Tasks as SignupViewTasks
from Libraries.Views.LoginView import Tasks as LoginViewTasks
from Libraries.Views.CartView import Tasks as CartViesTasks
from Libraries.Views.CheckoutView import Tasks as CheckoutViewTasks

class CreateContextTasks:
    """
    Creates all core objects and stores them in CTX.
    Must be executed before running any test cases.
    Responsible for creating and destroying the Browser context.
    This is the Robot-facing setup/teardown layer.

    - setup_browser(): initializes UIClient and registers view-level Tasks into CTX
    - teardown_browser(): closes browser and clears CTX references

    This follows the same architecture pattern used in Abloy SafeaBrowser:
    CTX.client  -> global browser client
    CTX.signup  -> global Signup view Tasks object
    
    """
    def setup_browser(self, url, headless=False):
        """
        Initialize Browser + Context + Page.
        Register SignupView.Tasks inside the global CTX object.
        """
        CTX.client = UIClient(url, headless=headless) # Create UIClient
        CTX.main_tasks = MainTasks(CTX.client)
        CTX.signup = SignupViewTasks(CTX.client)
        CTX.login = LoginViewTasks(CTX.client)
        CTX.cart = CartViesTasks(CTX.client)
        CTX.checkout = CheckoutViewTasks(CTX.client)

    def teardown_browser(self):
        """
        Close browser safely and clear CTX references.
        """
        if getattr(CTX, "client", None) is not None:
            CTX.client.close_browser()
        CTX.client = None
        CTX.signup = None

