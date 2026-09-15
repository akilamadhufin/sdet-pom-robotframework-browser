*** Settings ***
Library    ../Libraries/CreateContextTasks.py    AS    Context
Library    ../Libraries/UILibrary/SignupTasks.py

Test Setup    Context.Setup Browser    https://automationexercise.com
Test Teardown    Context.Teardown Browser 

*** Test Cases ***
Register New User And Login Successfully
    [Documentation]    Verify that a new user can be registered successfully
    [Tags]    signup    regression    smoke 
    Register New User   Akila    akila@example.com    12345    10    5    1995
    ...    Akila    Randunu    Abloy    Street 1    Street 2
    ...    Canada    Kandy    Gampaha    20000    0712345678
    
         