*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
Test Kuukausihavainnot Button
    Open Browser    https://www.ilmatieteenlaitos.fi/havaintojen-lataus    chrome
    Maximize Browser Window
    Sleep    3
    Wait Until Element Is Visible    xpath=//button[normalize-space(.)='Kuukausihavainnot']    timeout=15s
    Click Element                    xpath=//button[normalize-space(.)='Kuukausihavainnot']
    Sleep    2
    Close Browser
