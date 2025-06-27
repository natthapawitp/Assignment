*** Settings ***
Library           SeleniumLibrary
Library           ExcelKeywords.py
Library           Collections

Suite Setup       Load Excel Data
Suite Teardown    Close Browser

*** Variables ***
${EXCEL_FILE}     test_data.xlsx
${SHEET_NAME}     Sheet1
${URL}            https://your-web-app-url/login

*** Test Cases ***
Click App ID From Excel
    Open Browser    ${URL}    chrome
    Maximize Browser Window
    ${row}=    Get Excel Row By App ID    APP-01
    ${app_id}=    Set Variable    ${row["App ID"]}
    Log    จะคลิกที่ ${app_id} บนเว็บ
    Click Element By Text    ${app_id}
    Sleep    2

*** Keywords ***
Load Excel Data
    ${data}=    Read All Rows    ${EXCEL_FILE}    ${SHEET_NAME}
    Set Suite Variable    ${EXCEL_DATA}    ${data}

Get Excel Row By App ID
    [Arguments]    ${app_id}
    :FOR    ${row}    IN    @{EXCEL_DATA}
    \    IF    '${row["App ID"]}' == '${app_id}'
    \        [Return]    ${row}
    \    END
    [Return]    {}

Click Element By Text
    [Arguments]    ${text}
    ${xpath}=    Set Variable    //*[contains(text(),"${text}")]
    Wait Until Element Is Visible    xpath=${xpath}    10s
    Click Element    xpath=${xpath}
