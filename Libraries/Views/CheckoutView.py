from Libraries.UIClient import UIClient

class Actions:
    """
    Low-level UI actions for Checkout and Payment.
    """

    # -------- STATIC LOCATORS --------
    PROCEED_TO_CHECKOUT_BUTTON = "//a[contains(text(),'Proceed To Checkout')]"
    PLACE_ORDER_BUTTON = "//a[contains(text(),'Place Order')]"

    NAME_ON_CARD = "//input[@name='name_on_card']"
    CARD_NUMBER = "//input[@name='card_number']"
    CVC = "//input[@name='cvc']"
    EXPIRY_MONTH = "//input[@name='expiry_month']"
    EXPIRY_YEAR = "//input[@name='expiry_year']"

    PAY_BUTTON = "//button[contains(text(),'Pay')]"
    ORDER_SUCCESS_MESSAGE = "//p[contains(text(),'Congratulations! Your order has been confirmed!')]"

    DOWNLOAD_INVOICE_BUTTON = "//a[contains(text(),'Download Invoice')]"
    CONTINUE_BUTTON = "//a[contains(text(),'Continue')]"


    def __init__(self, client: UIClient):
        self.client = client

    def click_proceed_to_checkout(self):
        self.client.click_w(self.PROCEED_TO_CHECKOUT_BUTTON)

    def click_place_order(self):
        self.client.click_w(self.PLACE_ORDER_BUTTON)

    def fill_payment_details(self, name, card_number, cvc, month, year):
        self.client.type_text(self.NAME_ON_CARD, name)
        self.client.type_text(self.CARD_NUMBER, card_number)
        self.client.type_text(self.CVC, cvc)
        self.client.type_text(self.EXPIRY_MONTH, month)
        self.client.type_text(self.EXPIRY_YEAR, year)

    def click_pay_button(self):
        self.client.click_w(self.PAY_BUTTON)

    def wait_for_order_success(self):
        self.client.wait_for_element_to_be_visible(self.ORDER_SUCCESS_MESSAGE)   

    def click_download_invoice(self):
        self.client.click_w(self.DOWNLOAD_INVOICE_BUTTON)   

    def click_continue(self):
        self.client.click_w(self.CONTINUE_BUTTON)


class Tasks:
    """
    High-level workflow for Checkout and Payment.
    """ 

    def __init__(self, client: UIClient):
        self.actions = Actions(client)

    def proceed_to_checkout(self):
        self.actions.click_proceed_to_checkout()

    def place_order(self):
        self.actions.click_place_order()

    def complete_payment(self, name, card_number, cvc, month, year):
        self.actions.fill_payment_details(name, card_number, cvc, month, year)
        self.actions.click_pay_button()
        self.actions.wait_for_order_success()

    def download_invoice_and_continue(self):
        self.actions.click_download_invoice()
        self.actions.click_continue()                                             