from Libraries.ContextHolder import CTX

class ContactUsTasks:
    """
    Robot-facing keyword layer for Cart operations.
    Delegates to CTX.contactus (ContactUsView.Tasks).
    """

    def submit_contact_us_form(self, name, email, subject, message, file_path):
        CTX.main_tasks.go_contact_us()
        CTX.contactus.submit_contact_us_form(name, email, subject, message, file_path)
