*** Settings ***
Library         SeleniumLibrary

*** Variables ***
${username_locator}            id:user-name
${password_locator}            xpath://input[@type="password"]
${login_btn_locator}           id:login-button
${login_err_msg_locator}       xpath://h3[@data-test="error"]
    
*** Keywords ***
Login To SwagLabs
    [Arguments]    ${username}      ${password}
    Wait Until Element Is Visible    locator=${username_locator}
    Input Text    locator=${username_locator}    text=${username}
    Input Text    locator=${password_locator}    text=${password}
    Click Button    locator=${login_btn_locator}


Login Error Message Should Be
    [Arguments]    ${exp_err_msg}
    Wait Until Element Is Visible    locator=${login_err_msg_locator}
    ${act_err_msg}    Get Text   locator=${login_err_msg_locator}
    Should Be Equal As Strings    first=${act_err_msg}    second=${exp_err_msg}    msg=Actual login error message does not match the expected error message