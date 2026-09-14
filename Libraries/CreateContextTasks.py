from Libraries.ContextHolder import CTX
from Libraries.UIClient import UIClient
from Libraries.UILibrary.MainTasks import MainTasks

class CreateContextTasks:
    """
    Creates all core objects and stores them in CTX.
    Must be executed before running any test cases.
    """
    def __init__(self, url):
        CTX.client = UIClient(url) # Create UIClient
        CTX.main_tasks = MainTasks(CTX.main_tasks)