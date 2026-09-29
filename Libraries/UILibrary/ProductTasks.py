from Libraries.ContextHolder import CTX

class ProductTasks:
    """
    Robot-facing keyword layer for Cart operations.
    Delegates to CTX.products (ProductViewTasks).
    """

    def search_product_and_verify(self, product_keyword):
        CTX.main_tasks.give_data_consent()
        CTX.main_tasks.go_products()
        CTX.products.search_product(product_keyword)
        CTX.products.verify_products_in_result(product_keyword)

    def open_product_details_add_review_and_verify(self, product_name, name, email, review):
        CTX.main_tasks.give_data_consent()
        CTX.main_tasks.go_products()
        CTX.products.search_product(product_name)
        CTX.products.open_product_details(product_name)
        CTX.products.add_product_review_and_verify(name, email, review)