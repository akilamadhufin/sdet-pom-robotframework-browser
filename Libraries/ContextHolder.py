from Libraries.UIClient import UIClient
from Libraries.UILibrary.MainTasks import MainTasks
from Libraries.Views.SignupView import Tasks as SignupViewTasks
from Libraries.Views.LoginView import Tasks as LoginViewTasks

class Context:
    """
    Context holder for shared objects.
    """
    client: UIClient
    main_tasks: MainTasks
    signup: SignupViewTasks
    login: LoginViewTasks

CTX = Context()    
