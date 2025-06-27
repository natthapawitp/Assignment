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
Verify All App Data Dynamic
    Open Browser    ${URL}    chrome
    Maximize Browser Window

    FOR    ${row}    IN    @{EXCEL_DATA}
        ${app_id}=       Set Variable    ${row["App ID"]}
        ${expected_amount}=    Set Variable    ${row["Amount"]}
        Log    กำลังคลิกและตรวจสอบ App ID: ${app_id}

        Click App ID In Table    ${app_id}

        ${actual_amount}=    Get Amount From Detail Page
        Should Be Equal As Numbers    ${actual_amount}    ${expected_amount}
    END

*** Keywords ***
Load Excel Data
    ${data}=    Read All Rows    ${EXCEL_FILE}    ${SHEET_NAME}
    Set Suite Variable    ${EXCEL_DATA}    ${data}

Click App ID In Table
    [Arguments]    ${app_id}
    ${xpath}=    Set Variable    //table//tr[td[contains(normalize-space(.),"${app_id}")]]
    Wait Until Element Is Visible    xpath=${xpath}    timeout=10s
    Click Element    xpath=${xpath}

Get Amount From Detail Page
    # ดึงจำนวนเงินในหน้ารายละเอียด (ปรับตามจริง)
    Wait Until Element Is Visible    id=amountValue    timeout=10s
    ${text}=    Get Text    id=amountValue
    ${amount}=    Convert To Number    ${text}
    [Return]    ${amount}
