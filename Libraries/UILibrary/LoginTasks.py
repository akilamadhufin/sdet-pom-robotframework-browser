from Libraries.ContextHolder import CTX

class LoginTasks:
    """
    Robot-facing keyword layer.
    Delegates to CTX.login (LoginView.Tasks).
    """

    def logout_user(self):
        CTX.login.click_logout()

    def login_user(self, email, password):
        CTX.main_tasks.give_data_consent()
        CTX.main_tasks.go_home()
        CTX.main_tasks.go_signup_login()
        CTX.login.user_login(email, password)

    def verify_user_login(self, name):
        CTX.login.verify_user_login_correctly(name)

    def delete_user_account_and_verify(self, name):
        CTX.login.delete_account_and_verify(name)          
