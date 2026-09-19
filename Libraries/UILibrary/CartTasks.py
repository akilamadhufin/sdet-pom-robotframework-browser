from Libraries.ContextHolder import CTX

class CartTasks:
    """
    Robot-facing keyword layer for Cart operations.
    Delegates to CTX.cart (CartView.Tasks).
    """

    def add_cloth_products(self, *products):
        CTX.main_tasks.go_products()
        CTX.cart.add_cloth_products(products)


    def verify_cloth_in_cart(self, *products):
        CTX.main_tasks.go_cart()
        CTX.cart.verify_cloth_in_cart(products)    
