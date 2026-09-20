*** Settings ***
Library    ../Libraries/CreateContextTasks.py    AS    Context
Library    ../Libraries/UILibrary/SignupTasks.py
Library    ../Libraries/UILibrary/LoginTasks.py
Library    ../Libraries/UILibrary/ContactUsTasks.py
Resource    ../Resources/API.resource

Test Setup    Context.Setup Browser    https://automationexercise.com
Test Teardown    Context.Teardown Browser 

*** Test Cases ***
Register New User And Login Successfully
    [Documentation]    Verify that a new user can be registered successfully
    [Tags]    signup    regression    smoke 
    SignupTasks.Register New User   AkilaR    akila@example.com    12345    10    5    1995
    ...    Akila    Randunu    Abloy    Street 1    Street 2
    ...    Canada    Kandy    Gampaha    20000    0712345678
    SignupTasks.Verify User Registration Successfully    AkilaR        
    LoginTasks.Logout User
    [Teardown]    Cleanup Test User    akila@example.com

User Can Login Successfully
    [Documentation]    Verify that a new user can login successfully
    [Tags]    signup    regression    smoke
    LoginTasks.Login User    testemail@comp.com    12345
    LoginTasks.Verify User Login    testuser1
    LoginTasks.Logout User


User Can Submit Contact Us Form Successfully
    [Documentation]    Verify Contact Us form submission with file upload
    [Tags]    contactus    regression    smoke
    LoginTasks.Login User    testemail@comp.com    12345
    LoginTasks.Verify User Login    testuser1
    ContactUsTasks.Submit Contact Us Form    
        ...    Akila Randunu
        ...    akila@example.com
        ...    Inquiry About Product
        ...    Hello, this is a test message.
        ...    ${CURDIR}/../TestData/invoice.txt    
    LoginTasks.Logout User


    
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