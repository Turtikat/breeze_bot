*** Settings ***
Library    SeleniumLibrary
Library    Collections
Library    OperatingSystem

*** Variables ***
${URL}    https://www.ilmatieteenlaitos.fi/havaintojen-lataus
${BROWSER}    chrome
${CSV_FILE}    weather_data.csv

*** Test Cases ***
Get Weather Data
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Sleep    2s  # Odotetaan, että sivu latautuu

    # Suljetaan evästeikkuna
    Wait Until Element Is Visible    xpath=//button[contains(text(),'Salli kaikki evästeet')]    timeout=5s
    Click Element    xpath=//button[contains(text(),'Salli kaikki evästeet')]
    Sleep    2s  

    # Klikataan "Päivittäishavainnot"-välilehteä
    Click Element    id=tab-2
    Sleep    2s  

    # Klikataan "Hae tiedot" -painiketta
    Click Element    xpath=//button[contains(text(),'Hae tiedot')]
    Sleep    5s  # Odotetaan, että data latautuu

    # Haetaan taulukon sisältö
    ${weather_data}=    Get Text    xpath=//table[@id='data-table']
    Log To Console    ${weather_data}

    # Tallennetaan tiedot CSV-muotoon
    Create File    ${CSV_FILE}    ${weather_data}

    # Otetaan kuvakaappaus
    Capture Page Screenshot

    Close Browser
