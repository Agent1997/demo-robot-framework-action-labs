from robot.api.deco import keyword
from SeleniumLibrary import SeleniumLibrary


class Browser:
    
    def __init__(self, selenium_library: SeleniumLibrary):
        self.__selenium_library = selenium_library
        
    @keyword
    def open_swaglabs_in_chrome_browser(self):
        """This will spawn a browser and open the Swaglabs login page."""
        self.__selenium_library.open_browser(url='https://www.saucedemo.com/v1/', browser='chrome')
        self.__selenium_library.maximize_browser_window()
        
    @keyword
    def close_swaglabs(self):
        """This will close the Swaglabs browser."""
        self.__selenium_library.close_browser()