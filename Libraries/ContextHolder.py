from Libraries.UIClient import UIClient
from Libraries.UILibrary.MainTasks import MainTasks
from Libraries.Views.SignupView import Tasks as SignupViewTasks

class Context:
    """
    Context holder for shared objects.
    """
    client: UIClient
    main_tasks: MainTasks
    signup: SignupViewTasks

CTX = Context()    
