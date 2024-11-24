from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import time


class FormPage:
    def __init__(self, driver):
        #ambil dulu webdrivernya
        self.driver = driver
        # ambil semua locator element
        self.dropdownbox_click = (By.TAG_NAME, "option")
        self.checkbox_click = (By.XPATH, "//input[@id='chk_hospotal_readmission']")
        self.radio_button = (By.XPATH, "//input[@id='radio_program_medicaid']")
        self.radio_button_change = (By.XPATH, "//input[@id='radio_program_none']")
        self.calendar_click = (By.XPATH, "//div[@class='input-group-addon']")
        self.month_year_display = (By.XPATH, "//th[@class='datepicker-switch']")
        self.prev_button = (By.XPATH, "//th[@class='prev']")
        self.next_button = (By.XPATH, "//th[@class='next']")
        self.days = (By.XPATH, "//td[@class='day']")
        self.comment_input = (By.XPATH, "//textarea[@id='txt_comment']")
        self.book_click = (By.XPATH, "//button[@id='btn-book-appointment']")

    def dropdownbox_loop(self):
        #ambil 'Seoul CURA Healthcare Center' dari dropdown.
        options = self.driver.find_elements(*self.dropdownbox_click)
        for option in options:
            if option.text == "Seoul CURA Healthcare Center":
                option.click()
                break

    def checkbox_check(self):
        #klik checkbox
        self.driver.find_element(*self.checkbox_click).click()

    def radio_button_click(self):
        #ambil radiobutton medicaid
        self.driver.find_element(*self.radio_button).click()

    def radio_button_swap(self):
        #ganti radio button jadi none
        self.driver.find_element(*self.radio_button_change).click()

    def calendar_input(self):
        #klik calendarnya biar bisa keluar pop up calenda
        self.driver.find_element(*self.calendar_click).click()

    def loop_calendar(self):
        #pilih tanggal spesifik
        target_month = "December 2024"
        target_day = "8"
        
        #pisahin angka tahun dibelakang buat di compare
        target_datetime = datetime.strptime(target_month, "%B %Y")

        while True:
            # dapetin tahun dan bulan di calendar
            current_display = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.month_year_display)
            ).text
            #pisahin angka di tahun dan bulan calendar buat di compare
            current_datetime = datetime.strptime(current_display, "%B %Y")

            if current_datetime == target_datetime:
                break  # target bulan dan tahun sesuai

            # kalo ternyata tahun/bulan diatas
            if target_datetime < current_datetime:
                self.driver.find_element(*self.prev_button).click()
            #kalo ternyata tahun/bulan dibawah
            else:
                self.driver.find_element(*self.next_button).click()

            time.sleep(1)  # kasi sleep biar ke update

        # ambil tanggal
        days = self.driver.find_elements(*self.days)
        for day in days:
            if day.text == target_day: #ambil text di dalem element
                day.click() #kalo udah sesuai klik
                break

    def comment(self):
    #taro comment di field comment
        comment_box = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.comment_input)
        )
        comment_box.send_keys("Medical Check Up")

    def book(self):
        #submit
        self.driver.find_element(*self.book_click).click()
