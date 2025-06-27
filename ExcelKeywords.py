*** Settings ***
Library    ExcelKeywords.py
Library    Collections

*** Variables ***
${EXCEL_FILE}     test_data.xlsx
${SHEET_NAME}     Sheet1

*** Test Cases ***
Read Excel And Print Data
    ${rows}=    Read All Rows    ${EXCEL_FILE}    ${SHEET_NAME}
    Log Many    ${rows}
