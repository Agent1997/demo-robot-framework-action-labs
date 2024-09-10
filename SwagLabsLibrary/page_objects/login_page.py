from SeleniumLibrary import SeleniumLibrary
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from SwagLabsLibrary.page_locators import login_page_locators

class LoginPage:
    
    def __init__(self, selenium_library: SeleniumLibrary):
        self.__selenium_library = selenium_library
        
    @keyword
    def user_login_to_swaglabs(self, username: str, password: str):
        """This will attempt to login the user using the username and password provided."""
        self.__selenium_library.wait_until_element_is_visible(locator=login_page_locators.USERNAME_LOCATOR)
        self.__selenium_library.clear_element_text(locator=login_page_locators.USERNAME_LOCATOR)
        self.__selenium_library.input_text(locator=login_page_locators.USERNAME_LOCATOR, text=username)
        self.__selenium_library.clear_element_text(locator=login_page_locators.PASSWORD_LOCATOR)
        self.__selenium_library.input_text(locator=login_page_locators.PASSWORD_LOCATOR, text=password)
        self.__selenium_library.click_button(locator=login_page_locators.LOGIN_BTN_LOCATOR)
        
    @keyword
    def user_should_see_that_login_error_message_is(self, exp_err_msg: str):
        """This checks the error message displayed in the login page if a user attempts to login using an invalid credential."""
        self.__selenium_library.wait_until_element_is_visible(locator=login_page_locators.LOGIN_ERR_MSG_LOCATOR)
        act_err_msg = self.__selenium_library.get_text(locator=login_page_locators.LOGIN_ERR_MSG_LOCATOR)
        BuiltIn().should_be_equal_as_strings(first=act_err_msg, second=exp_err_msg, msg="Actual login error message does not match the expected error message")