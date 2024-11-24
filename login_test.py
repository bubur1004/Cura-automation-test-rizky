import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager #biar pytest nya tau chromedrivermanager(kalo engga gini gabisa di run gatau knp)
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import time
from login_page import LoginPage #import dulu page yang ada semua param, function, element locator biar yang udah kita set bisa tinggal dipanggil


@pytest.fixture #buat bikin fixture
def driver():
# Panggil chromedriver harus gini kalo pake fixture
    service = Service(ChromeDriverManager().install()) # pastiin pake ini biar chromedrivermanagernya kepake klo engga nanti chromedrivermanagernya ke gray dan gakepake
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(10)  # Optional: Implicit wait ada buat nunggu element dulu sebelom action
    yield driver  # biar bisa manggil driver sebagai function di test case lain
    driver.quit()  # buat kasi tau klo di akhir bakalan quit

def test_cura_web(driver: WebDriver):
    login_page = LoginPage(driver) #panggil driver di file login_page
    login_page.open_page("https://katalon-demo-cura.herokuapp.com/") #panggil def open_page
    login_page.maximize_window() #panggil def maximize_window
    login_page.click_appointment() #panggil def click_appointment
    time.sleep(2)
    login_page.enter_username("John Doe")
    time.sleep(2)
    login_page.enter_password("ThisIsNotAPassword")
    time.sleep(2)
    login_page.click_login()
    time.sleep(5)
    