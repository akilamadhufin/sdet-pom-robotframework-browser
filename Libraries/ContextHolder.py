from Libraries.UIClient import UIClient
from Libraries.UILibrary.MainTasks import MainTasks
from Libraries.Views.SignupView import Tasks as SignupViewTasks
from Libraries.Views.LoginView import Tasks as LoginViewTasks
from Libraries.Views.CartView import Tasks as CartViewTasks
from Libraries.Views.CheckoutView import Tasks as CheckoutViewTasks
from Libraries.Views.ContactUsView import Tasks as ContactUsViewTasks

class Context:
    """
    Context holder for shared objects.
    """
    client: UIClient
    main_tasks: MainTasks
    signup: SignupViewTasks
    login: LoginViewTasks
    cart: CartViewTasks
    checkout: CheckoutViewTasks
    contactus: ContactUsViewTasks

CTX = Context()    
