from Libraries.ContextHolder import CTX

class SignupTasks:
    """
    Robot-facing keyword layer.
    Delegates to CTX.signup (SignupView.Tasks).
    """

    def register_new_user(self, name, email, password, day, month, year,
                      first_name, last_name, company, address1, address2,
                      country, state, city, zipcode, mobile):
        CTX.main_tasks.give_data_consent()
        CTX.main_tasks.go_home()
        CTX.main_tasks.go_signup_login()
        CTX.signup.register_user(name, email, password, day, month, year,
            first_name, last_name, company, address1, address2,
            country, state, city, zipcode, mobile,)
