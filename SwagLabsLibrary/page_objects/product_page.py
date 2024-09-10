from SeleniumLibrary import SeleniumLibrary
from robot.api.deco import keyword
from SwagLabsLibrary.page_locators import products_page_locators

class ProductsPage:
    
    def __init__(self, selenium_library: SeleniumLibrary):
        self.__selenium_library = selenium_library
        
        
    @keyword
    def user_should_be_in_the_product_page(self):
        """This checks if current page is the Products page by checking the page label."""
        self.__selenium_library.wait_until_element_is_visible(locator=products_page_locators.PRODUCTS_PAGE_LABEL, error="Products page label is not visible.")
    