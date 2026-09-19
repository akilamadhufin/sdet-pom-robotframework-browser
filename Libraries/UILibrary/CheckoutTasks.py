from Libraries.ContextHolder import CTX

class CheckoutTasks:
    """
    Robot-facing keyword layer for Checkout operations.
    Delegates to CTX.checkout (CheckoutView.Tasks).
    """

    def proceed_to_checkout(self):
        # Must be on Cart page first
        CTX.main_tasks.go_cart()
        CTX.checkout.proceed_to_checkout()

    def place_order(self):
        CTX.checkout.place_order()

    def complete_payment(self, name, card_number, cvc, month, year):
        CTX.checkout.complete_payment(name, card_number, cvc, month, year)

    def download_invoice_and_continue(self):
        CTX.checkout.download_invoice_and_continue()        