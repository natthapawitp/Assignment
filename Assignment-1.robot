*** Settings ***
Library    RequestsLibrary
Library    JSONLibrary

*** Variable ***
${endpoint_get_profile}   https://reqres.in/api

***Test Cases ***
Assignment 1:
    Create Session     Get_User_Profile    ${endpoint_get_profile}
    &{headers}=    Create Dictionary    Content-Type=application/json
    ${params}=    Create Dictionary    page=2
    ${response}=    GET On Session    Get_User_Profile    /users    headers=${headers}    params=&{params}    expected_status=200
    Log    ${response.json()}
    Should Be Equal As Strings    ${response.json()['total_pages']}    2
    Should Be Equal As Strings    ${response.status_code}    200
    ${filter.json()}=    Get Value From Json    ${response.json()}    $..data[?(@.email == 'byron.fields@reqres.in')]
    Log    ${filter.json()}