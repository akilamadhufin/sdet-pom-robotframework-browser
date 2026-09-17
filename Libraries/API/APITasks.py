# APITasks.py
# ---------------------------------------------------------
# Task layer:
# - Uses robot_rename decorator
# - Automatically exposes Robot Framework keywords
# - Adds suffix: "API T"
# - Contains business logic and validations
# ---------------------------------------------------------

from robotlibcore import keyword
from Libraries.API.APIEndpoints import APIEndpoints

def robot_rename(func):
    """
    Converts method name into a Robot Framework keyword.
    Example:
        login_user -> Login User - API T
    """
    keyword_name = func.__name__.replace("_", " ").title() + " - API T"
    return keyword(keyword_name)(func)

class APITasks:
    """
    Task layer.
    Contains business logic combining multiple endpoints.
    Automatically exposed as Robot Framework keywords.
    """

    def __init__(self, client):
        # Tasks do NOT use the HTTP client directly.
        # Tasks use ENDPOINTS, which use the client.
        self.endpoints = APIEndpoints(client)

    # -----------------------------------------------------
    # User Account Tasks
    # -----------------------------------------------------

    @robot_rename
    def login_user(self, email: str, password: str):
        """
        Calls verify_login and validates the response.
        """
        response = self.endpoints.verify_login(email, password)

        if response.status_code != 200:
            raise AssertionError(f"Login Failed: {response.message}")

        return response

    @robot_rename
    def create_user_and_verify(self, name: str, email: str, password: str, title: str,
                               birth_day: int, birth_month: int, birth_year: int,
                               first_name: str, last_name: str, company: str,
                               address1: str, address2: str, country: str,
                               state: str, city: str, zipcode: str, mobile_number: str):
        """
        Creates a user and verifies creation by fetching user details.
        """
        create_response = self.endpoints.create_account(
            name, email, password, title,
            birth_day, birth_month, birth_year,
            first_name, last_name, company,
            address1, address2, country,
            state, city, zipcode, mobile_number
        )
        if create_response.status_code != 200:
            raise AssertionError(f"User creation failed: {create_response.message}")
        
        verify_response = self.endpoints.get_user_by_email(email)

        if verify_response.status_code != 200:
            
            raise AssertionError(f"User verification failed: {verify_response.message}")

        return verify_response

    @robot_rename
    def delete_user_and_verify(self, email: str, password: str):
        """
        Deletes a user and confirms deletion.
        """
        delete_response = self.endpoints.delete_account(email, password)

        if delete_response.status_code != 200:
            raise AssertionError(f"User deletion failed: {delete_response.message}")

        verify_response = self.endpoints.get_user_by_email(email)

        if verify_response.status_code == 200:
            raise AssertionError(f"User still exists after deletion.")

        return delete_response

    # -----------------------------------------------------
    # Product Tasks
    # -----------------------------------------------------    

    @robot_rename
    def search_product_and_validate(self, search_text: str):
        """
        Searches for a product and validates the result.
        """
        response = self.endpoints.search_product(search_text)

        if response.status_code != 200:
            raise AssertionError(f"Product search failed: {response.message}")

        if not response.data:
            raise AssertionError(f"No products found for search text.")

        return response

    @robot_rename
    def get_all_products_and_validate(self):
        """
        Fetches all products and validates the list.
        """
        response = self.endpoints.get_all_products()

        if response.status_code != 200:
            raise AssertionError(f"Fetching products failed: {response.message}")

        if not response.data:
            raise AssertionError(f"Product list is empty.")

        return response

    # -----------------------------------------------------
    # Brand Tasks
    # -----------------------------------------------------
    
    @robot_rename
    def get_all_brands_and_validate(self):
        """
        Fetches all brands and validates the list.
        """
        response = self.endpoints.get_all_brands()

        if response.status_code != 200:
            raise AssertionError(f"Fetching brands failed: {response.message}")

        if not response.data:
            raise AssertionError("Brand list is empty.")

        return response