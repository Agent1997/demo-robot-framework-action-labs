*** Settings ***
Library         SeleniumLibrary

*** Variables ***
${products_page_label}        xpath://div[@class='product_label' and text() = 'Products']

*** Keywords ***
User should be in the product page 
    [Documentation]        This checks if current page is the Products page by checking the page label
    Wait Until Element Is Visible    locator=${products_page_label}    error=Products page label is not visible    