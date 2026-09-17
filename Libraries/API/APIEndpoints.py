# UserApiEndpoints.py
# ---------------------------------------------------------
# Endpoint layer:
# - Uses robot_rename decorator
# - Automatically exposes Robot Framework keywords
# - Adds suffix: "API E"
# - No business logic here
# ---------------------------------------------------------

from robotlibcore import keyword
from Libraries.API.APIClient import APIClient

def robot_rename(func):
    """
    Converts method name into a Robot Framework keyword.
    Example:
        verify_login -> Verify Login - User API E
    """
    keyword_name = func.__name__.replace("_"," ").title() + " - API E" # __name__ = convert the function’s name as a string
    return keyword(keyword_name)(func)


class APIEndpoints:
    """
    Endpoint layer.
    One method per API endpoint.
    Automatically exposed as Robot Framework keywords.
    """

    def __init__(self, client: APIClient):
        self.client = client

    # -----------------------------------------------------
    # User Account Endpoints
    # -----------------------------------------------------

    @robot_rename
    def create_account(self, name: str, email: str, password: str, title: str,
                       birth_day: int, birth_month: int, birth_year: int,
                       first_name: str, last_name: str, company: str,
                       address1: str, address2: str, country: str,
                       state: str, city: str, zipcode: str, mobile_number: str):

        payload = {
            "name": name, "email": email, "password": password, "title": title,
            "birth_day": birth_day, "birth_month": birth_month, "birth_year": birth_year,
            "firstname": first_name, "lastname": last_name, "company": company,
            "address1": address1, "address2": address2, "country": country,
            "state": state, "city": city, "zipcode": zipcode, "mobile_number": mobile_number
        }
        return self.client.post("createAccount", payload)

    @robot_rename
    def delete_account(self, email: str, password: str):
        payload = {"email": email, "password": password}
        return self.client.delete("deleteAccount", payload)

    @robot_rename
    def verify_login(self, email: str, password: str):
        payload = {"email": email, "password": password}
        return self.client.post("verifyLogin", payload)

    @robot_rename
    def get_user_by_email(self, email: str):
        params = {"email": email}
        return self.client.get("getUserDetailByEmail", params)

    # -----------------------------------------------------
    # Product Endpoints
    # -----------------------------------------------------

    @robot_rename
    def get_all_products(self):
        return self.client.get("productsList")

    @robot_rename
    def search_product(self, search_text: str):
        payload = {"search_product": search_text}
        return self.client.post("searchProduct", payload)

    # -----------------------------------------------------
    # Brand Endpoints
    # -----------------------------------------------------

    @robot_rename
    def get_all_brands(self):
        return self.client.get("brandsList")