*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}    https://www.ilmatieteenlaitos.fi/havaintojen-lataus#!/
${BROWSER}    Chrome

*** Test Cases ***
Open Weather Data Page
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Wait Until Page Contains    Havaintojen lataus

Select Observations
    # Tässä vaiheessa lisätään tarvittavat klikkaukset ja valinnat sivulta
    # Esimerkki:
    Click Element    xpath=//button[contains(text(),'Sää')]
    Sleep    2s
    Click Element    xpath=//span[contains(text(),'Lämpötila')]

Download Data
    # Klikataan latauspainiketta ja odotetaan lataus
    Click Button    xpath=//button[contains(text(),'Lataa')]
    Sleep    5s

Close Browser
    Close Browser

*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
Get Weather Data
    Open Browser    https://www.ilmatieteenlaitos.fi/havaintojen-lataus    chrome
    Maximize Browser Window
    Sleep    2s  # Odotetaan, että sivu latautuu

    # Jos evästeikkuna näkyy, suljetaan se
    Wait Until Element Is Visible    xpath=//button[contains(text(),'Salli kaikki evästeet')]    timeout=5s
    Click Element    xpath=//button[contains(text(),'Salli kaikki evästeet')]
    Sleep    2s  # Pieni odotus, että ikkuna sulkeutuu

    # Klikataan "Päivittäishavainnot"-välilehteä
    Click Element    id=tab-2
    Sleep    2s  # Odotetaan, että välilehti vaihtuu

    # Otetaan kuvakaappaus varmistukseksi
    Capture Page Screenshot

    # Suljetaan selain
    Close Browser


