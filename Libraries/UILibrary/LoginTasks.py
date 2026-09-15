from Libraries.ContextHolder import CTX

class LoginTasks:
    """
    Robot-facing keyword layer.
    Delegates to CTX.login (LoginView.Tasks).
    """

    def logout_user(self):
        CTX.login.click_logout()
