from Libraries.UIClient import UIClient
from Libraries.Views.MainView import MainView
from Libraries.UILibrary.MainTasks import MainTasks

class Context:
    """
    Context holder for shared objects.
    """
    client: UIClient
    main_tasks: MainTasks

CTX = Context()    
