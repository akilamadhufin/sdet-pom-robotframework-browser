from Libraries.UIClient import UIClient

class Actions:
    """
    Low-level UI actions for Products.
    """
    # -------- LOCATORS --------
    SEARCH_INPUT = "//input[@id='search_product']"
    SEARCH_BUTTON = "//button[@id='submit_search']"
    SEARCH_RESULT_PRODUCT_TEMPLATE = "//div[@class='productinfo text-center']/p"
    PRODUCT_INFO_XPATH = "//div[@class='productinfo text-center']//p[normalize-space(.)='REPLACE_ME']"
    VIEW_PRODUCT_BUTTON = "//div[@class='choose']//a[contains(@href,'product_details')]"

    REVIEW_NAME = "//input[@id='name']"
    REVIEW_EMAIL = "//input[@id='email']"
    REVIEW_TEXT = "//textarea[@id='review']"
    REVIEW_SUBMIT = "//button[@id='button-review']"
    REVIEW_SUCCESS = "//div[contains(@class,'alert-success')]//span[contains(text(),'Thank you for your review')]"

    def __init__(self, client:UIClient):
        self.client = client

    def search_product(self, product_keyword:str):
        self.client.type_text(self.SEARCH_INPUT,product_keyword)
        self.client.click_w(self.SEARCH_BUTTON)
        self.client.wait_until_page_idle()        

    def get_all_product_search_results(self):
        return self.client.get_texts(self.SEARCH_RESULT_PRODUCT_TEMPLATE)

    def open_product_details(self, product_name):
        locator = self.PRODUCT_INFO_XPATH.replace("REPLACE_ME", product_name)
        self.client.wait_for_element_to_be_visible(locator)
        self.client.click_w(self.VIEW_PRODUCT_BUTTON)
        self.client.wait_until_page_idle()

    def fill_add_review_form(self, name, email, review):
        self.client.type_text(self.REVIEW_NAME, name)
        self.client.type_text(self.REVIEW_EMAIL, email)
        self.client.type_text(self.REVIEW_TEXT, review)
        self.client.click_w(self.REVIEW_SUBMIT)

    def verify_product_review_submit(self):
        self.client.wait_for_element_to_be_visible(self.REVIEW_SUCCESS)        

class Tasks:
    """
    High-level workflow layer for products.
    """

    def __init__(self, client:UIClient):
        self.actions = Actions(client)

    def search_product(self, product_keyword):
        self.actions.search_product(product_keyword)

    def verify_products_in_result(self, product_keyword):
        results = self.actions.get_all_product_search_results()
        for item in results:
            if product_keyword.lower() in item.lower():
                return True
        raise AssertionError(f"No results matched keyword: {product_keyword}")    

    def open_product_details(self, product_name):
        self.actions.open_product_details(product_name)

    def add_product_review_and_verify(self, name, email, review):
        self.actions.fill_add_review_form(name, email, review)
        self.actions.verify_product_review_submit()    

