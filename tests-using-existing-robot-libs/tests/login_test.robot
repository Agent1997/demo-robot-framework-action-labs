*** Settings ***
Resource        ../keywords/login_page.resource
Resource        ../keywords/browser.resource
Resource        ../keywords/products_page.resource
Test Setup      Open SwagLabs in Chrome Browser
Test Teardown   Close SwagLabs  
Documentation    This test suite verifies that user with valid credentials can login to SwagLabs and user with invalid credentials cannot

*** Variables ***
${invalid_username_and_password_err_msg}          Epic sadface: Username and password do not match any user in this service
${locked_out_user_err_msg}                        Epic sadface: Sorry, this user has been locked out.
${username_required_err_msg}                      Epic sadface: Username is required
${password_required_err_msg}                      Epic sadface: Password is required
${valid_username}                                 standard_user
${valid_password}                                 secret_sauce

*** Test Cases ***
Verify that a user cannot login using invalid credentials
    [Template]    Verify logging in using invalid credentials
    ${valid_username}       invalid_password      ${invalid_username_and_password_err_msg}
    invalid_username        ${valid_password}     ${invalid_username_and_password_err_msg}
    invalid_username        invalid_password      ${invalid_username_and_password_err_msg}
    locked_out_user         ${valid_password}     ${locked_out_user_err_msg}

Verify that a user can login using a valid credentials
    User Login To SwagLabs    username=${valid_username}    password=${valid_password}
    User should be in the product page

*** Keywords ***
Verify logging in using invalid credentials
    [Arguments]    ${username}    ${password}    ${exp_err_msg}
    User Login To SwagLabs    username=${username}    password=${password}
    Users should see that login error message is    exp_err_msg=${exp_err_msg}
