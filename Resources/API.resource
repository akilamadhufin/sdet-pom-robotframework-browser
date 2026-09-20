*** Settings ***
# Load the Python API library once for all Robot tests using this resource.
Library    ../Libraries/API/API_RF.py    https://automationexercise.com/api

*** Keywords ***
Delete User Account Via API
    [Arguments]    ${email}    ${password}
    # Call the low-level endpoint keyword.
    ${response}=    Delete User And Verify - API T    ${email}    ${password}
    # Validate the API's application-level response.
    Should Be Equal As Integers    ${response.response_code}    200    msg=Account deletion failed: ${response.message}


Check User Exists Via API
    [Arguments]    ${email}
    ${response}=    Get User By Email - API E    ${email}
    ${code}=    Set Variable    ${response.response_code}
    ${exists}=    Evaluate    ${code} == 200
    RETURN    ${exists}    
