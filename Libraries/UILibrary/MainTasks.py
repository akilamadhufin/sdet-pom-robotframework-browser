from Libraries.Views.MainView import MainView

class MainTasks:
    """
    High-level navigation tasks for the AutomationExercise website.

    This class wraps MainView actions into business-level tasks.
    Tests should call these tasks instead of calling MainView directly.
    """

    def __init__(self,client):
        # CTX.main_view is created in CreateContextTasks.py
        self.view = MainView(client)

    def give_data_consent(self):
        self.view.give_data_consent()

    def go_home(self):
        """Navigate to the Home page."""
        self.view.go_home()

    def go_signup_login(self):
        """Navigate to the Signup/Login page."""
        self.view.go_signup_login()

    def go_products(self):
        """Navigate to the Products page."""
        self.view.go_products()

    def go_cart(self):
        """Navigate to the Cart page."""
        self.view.go_cart()

    def go_contact_us(self):
        """Navigate to the Contact Us page."""
        self.view.go_contact_us()

    def go_test_cases(self):
        """Navigate to the Test Cases page."""
        self.view.go_test_cases()

    def go_api_testing(self):
        """Navigate to the API Testing page."""
        self.view.go_api_testing()

    def go_video_tutorials(self):
        """Navigate to the Video Tutorials page."""
        self.view.go_video_tutorials()        
            