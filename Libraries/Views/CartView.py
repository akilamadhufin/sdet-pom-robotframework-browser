from Libraries.UIClient import UIClient

class Actions:
    """
    Low-level UI actions for Tops category and Cart.
    """

    # -------- LOCATORS --------
    WOMEN_CATEGORY = "//a[@href='#Women' and @data-toggle='collapse']"
    TOPS_SUBCATEGORY = "//a[@href='/category_products/2' and contains(text(),'Tops')]"
    CONTINUE_SHOPPING = "//button[contains(text(),'Continue Shopping')]"
    PRODUCT_ADD_BUTTON_TEMPLATE = ("//div[@class='productinfo text-center']/p[text()='REPLACE_ME']"
                                   "/../a[contains(@class,'add-to-cart')]")
    CART_ROW_TEMPLATE = "//td[@class='cart_description']//a[contains(text(),'REPLACE_ME')]"

    def __init__(self, client:UIClient):
        self.client = client

    def open_women_tops(self):
        self.client.click_w(self.WOMEN_CATEGORY)
        self.client.wait_for_element_to_be_visible(self.TOPS_SUBCATEGORY)
        self.client.click_w(self.TOPS_SUBCATEGORY)

    def add_product_to_cart(self, product_name: str):
        locator= self.PRODUCT_ADD_BUTTON_TEMPLATE.replace("REPLACE_ME", product_name)
        self.client.click_w(locator)
        self.client.click_w(self.CONTINUE_SHOPPING)

    def wait_product_in_cart(self, product_name: str):
        locator = self.CART_ROW_TEMPLATE.replace("REPLACE_ME", product_name)
        self.client.wait_for_element_to_be_visible(locator)


class Tasks:
    """
    High-level workflow layer for Tops + Cart.
    """

    def __init__(self, client: UIClient):
        self.actions = Actions(client)

    def add_cloth_products(self, product_list):
        self.actions.open_women_tops()
        for product in product_list:
            self.actions.add_product_to_cart(product)
 
    def verify_cloth_in_cart(self, product_list):
            for product in product_list:
                self.actions.wait_product_in_cart(product)    
