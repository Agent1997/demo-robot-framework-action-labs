from pathlib import Path
from typing import List
from SeleniumLibrary import SeleniumLibrary
from robotlibcore import DynamicCore
from robot.api.deco import library
from SwagLabsLibrary.page_objects.browser import Browser
from SwagLabsLibrary.page_objects.login_page import LoginPage
from SwagLabsLibrary.page_objects.product_page import ProductsPage

@library(scope='GLOBAL')
class SwagLabsLibrary(DynamicCore):
    """SwagLabsLibrary is a demo library that provides keywords to automate interaction with the Swag Labs demo application (https://www.saucedemo.com/v1/index.html).
    This library demonstrate the basic usage of `PythonLibCore` (https://github.com/robotframework/PythonLibCore) for creating custom Robot Framework library that suites your application.
    To learn more about robot framework, visit the following websites:
    - https://robotframework.org/ 
    - https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html
    NOTE: This is for demo purposes only! The construction of the keywords and the codes may be different in real projects and may be a little more complicated.
    """

    def __init__(self) -> None:
        self.__selenium_library = SeleniumLibrary(screenshot_root_directory='EMBED')
        components = [
            Browser(selenium_library=self.__selenium_library),
            LoginPage(selenium_library=self.__selenium_library),
            ProductsPage(selenium_library=self.__selenium_library)
            
        ]
        
        DynamicCore.__init__(self, library_components=components)