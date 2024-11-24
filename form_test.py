import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.webdriver import WebDriver
from Pages.login_page import LoginPage
from Pages.form_page import FormPage

import time


@pytest.fixture
def driver():
    #install dan quit chrome
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(10)  # buat nunggu element keluar
    yield driver
    driver.quit()  # Quit driver

@pytest.mark.parametrize("username, password", [
    ("John Doe", "ThisIsNotAPassword"),  # Valid credentials
    ("user2", "pass2"),  # Invalid credentials
    ("test", "test"),  # Invalid credentials
])


def test_cura_web(driver: WebDriver, username, password):
    #test case cura web
    
    # Step 1: Login
    login_page = LoginPage(driver)  # Jalanin dulu loginpage dan di set drivernya di loginpage
    login_page.open_page("https://katalon-demo-cura.herokuapp.com/")
    login_page.maximize_window()
    login_page.click_appointment()
    login_page.enter_username(username)
    login_page.enter_password(password)
    login_page.click_login()

    # Step 2: Fill Appointment Form
    form_page = FormPage(driver)  # jalanin dulu formpage dan di set drivernya di formpage soalnya belom di set
    form_page.dropdownbox_loop()  # panggil function dari form_page
    form_page.checkbox_check()  
    form_page.radio_button_click()  
    form_page.radio_button_swap()  
    form_page.calendar_input()  
    form_page.loop_calendar()  
    form_page.comment()
    form_page.book()  
    assert "Appointment Confirmation" in driver.page_source #pastiin ada text Appointment confirmation di akhir
    time.sleep(5)
