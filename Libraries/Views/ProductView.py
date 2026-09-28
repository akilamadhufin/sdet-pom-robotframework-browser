from Libraries.UIClient import UIClient

class Actions:
    """
    Low-level UI actions for Products.
    """
    # -------- LOCATORS --------
    SEARCH_INPUT = "//input[@id='search_product']"
    SEARCH_BUTTON = "//button[@id='submit_search']"
    SEARCH_RESULT_PRODUCT_TEMPLATE = "//div[@class='productinfo text-center']/p"

    def __init__(self, client:UIClient):
        self.client = client

    def search_product(self, product_keyword:str):
        self.client.type_text(self.SEARCH_INPUT,product_keyword)

    def get_all_product_search_results(self):
        return self.client.get_texts(self.SEARCH_RESULT_PRODUCT_TEMPLATE)


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
   