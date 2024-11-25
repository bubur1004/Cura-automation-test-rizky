import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.webdriver import WebDriver
from Pages.login_page import LoginPage
from Pages.form_page import FormPage
import time
import datetime

def take_screenshot(driver: WebDriver, step_name: str):
    """Take a screenshot and save it with the step name and timestamp."""
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{step_name}_{timestamp}.png"
    driver.save_screenshot(filename)



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
    take_screenshot(driver, "01_open_page")
    login_page.click_appointment()
    take_screenshot(driver, "02_click_appointment")
    login_page.enter_username(username)
    login_page.enter_password(password)
    login_page.click_login()
    take_screenshot(driver, "03_login")
    

    # Step 2: Fill Appointment Form
    form_page = FormPage(driver)  # jalanin dulu formpage dan di set drivernya di formpage soalnya belom di set
    form_page.dropdownbox_loop()  # panggil function dari form_page
    take_screenshot(driver, "04_dropdown_selected")
    form_page.checkbox_check()  
    form_page.radio_button_click()  
    form_page.radio_button_swap()  
    form_page.calendar_input()  
    form_page.loop_calendar()  
    form_page.comment()
    take_screenshot(driver, "05_form_full") 
    form_page.book()
    take_screenshot(driver, "06_booking")  
    assert "Appointment Confirmation" in driver.page_source #pastiin ada text Appointment confirmation di akhir
    time.sleep(5)
