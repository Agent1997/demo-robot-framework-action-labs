*** Settings ***
Library        SeleniumLibrary 

*** Keywords ***
Open SwagLabs in Chrome Browser
    Open Browser    url=https://www.saucedemo.com/v1/    browser=chrome   
    Maximize Browser Window


Close SwagLabs
    Close All Browsers    