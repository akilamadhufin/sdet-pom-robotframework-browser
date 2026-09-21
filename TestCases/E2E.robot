*** Settings ***
Library    ../Libraries/CreateContextTasks.py    AS    Context
Library    ../Libraries/UILibrary/SignupTasks.py
Library    ../Libraries/UILibrary/LoginTasks.py
Library    ../Libraries/UILibrary/CartTasks.py
Library    ../Libraries/UILibrary/CheckoutTasks.py
Resource    ../Resources/API.resource

Test Setup    Context.Setup Browser    https://automationexercise.com
Test Teardown    Context.Teardown Browser 

*** Variables ***
${CARD_NAME}          Akila Randunu
${CARD_NUMBER}        4242424242424242
${CVC}                123
${EXP_MONTH}          12
${EXP_YEAR}           2026

${PRODUCT_1}       Blue Top
${PRODUCT_2}       Winter Top
${PRODUCT_3}       Summer White Top

*** Test Cases ***
User Can Register, Add Products To Cart And Checkout
    [Documentation]    Full E2E flow: Signup Add products → Cart → Checkout → Payment → Invoice
    [Tags]    signup    regression    smoke    E2E    Production
    SignupTasks.Register New User   AkilaR    akila@example.com    12345    10    5    1995
    ...    Akila    Randunu    Abloy    Street 1    Street 2
    ...    Canada    Kandy    Gampaha    20000    0712345678
    SignupTasks.Verify User Registration Successfully    AkilaR

    CartTasks.Add Cloth Products    ${PRODUCT_1}    ${PRODUCT_2}    ${PRODUCT_3}
    CartTasks.Verify Cloth In Cart    ${PRODUCT_1}    ${PRODUCT_2}    ${PRODUCT_3}
    CheckoutTasks.Proceed To Checkout
    CheckoutTasks.Place Order
    CheckoutTasks.Complete Payment    ${CARD_NAME}    ${CARD_NUMBER}    ${CVC}    ${EXP_MONTH}    ${EXP_YEAR}
    CheckoutTasks.Download Invoice And Continue
    LoginTasks.Logout User
    [Teardown]    Cleanup Test User    akila@example.com

User Can Register, Login, Add Products To Cart, Checkout And Delete Account
    [Documentation]    Full E2E flow: Signup → Login → Add products → Cart → Checkout → Payment → Invoice → Delete Account
    [Tags]    signup    regression    smoke    E2E    Production
    SignupTasks.Register New User   AkilaR    akila@example.com    12345    10    5    1995
    ...    Akila    Randunu    Abloy    Street 1    Street 2
    ...    Canada    Kandy    Gampaha    20000    0712345678
    SignupTasks.Verify User Registration Successfully    AkilaR
    LoginTasks.Logout User
    LoginTasks.Login User    akila@example.com    12345
    CartTasks.Add Cloth Products    ${PRODUCT_1}    ${PRODUCT_2}    ${PRODUCT_3}
    CartTasks.Verify Cloth In Cart    ${PRODUCT_1}    ${PRODUCT_2}    ${PRODUCT_3}
    CheckoutTasks.Proceed To Checkout
    CheckoutTasks.Place Order
    CheckoutTasks.Complete Payment    ${CARD_NAME}    ${CARD_NUMBER}    ${CVC}    ${EXP_MONTH}    ${EXP_YEAR}
    CheckoutTasks.Download Invoice And Continue
    LoginTasks.Delete User Account And_Verify    AkilaR       
    [Teardown]    Cleanup Test User    akila@example.com



*** Keywords ***
Cleanup Test User
    [Arguments]    ${email}
    ${exists}=    Check User Exists Via API    ${email}
    IF    ${exists}
        Delete User Account Via API    ${email}    12345
    ELSE
        Log    User ${email} already deleted, skipping cleanup.    INFO
    END    
    Context.Teardown Browser