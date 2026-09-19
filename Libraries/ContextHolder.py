from Libraries.UIClient import UIClient
from Libraries.UILibrary.MainTasks import MainTasks
from Libraries.Views.SignupView import Tasks as SignupViewTasks
from Libraries.Views.LoginView import Tasks as LoginViewTasks
from Libraries.Views.CartView import Tasks as CartViesTasks
from Libraries.Views.CheckoutView import Tasks as CheckoutViewTasks

class Context:
    """
    Context holder for shared objects.
    """
    client: UIClient
    main_tasks: MainTasks
    signup: SignupViewTasks
    login: LoginViewTasks
    cart: CartViesTasks
    checkout: CheckoutViewTasks

CTX = Context()    
