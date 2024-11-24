from selenium.webdriver.common.by import By


class LoginPage:
    
    def __init__(self, driver):
        """Initialize the LoginPage object with WebDriver."""
        self.driver = driver
        # Define locators
        self.username_textbox = (By.ID, "txt-username")
        self.password_textbox = (By.ID, "txt-password")
        self.login_button = (By.ID, "btn-login")
        self.appointment_click = (By.ID, "btn-make-appointment")

    def open_page(self, url):
        """Navigate to the specified URL."""
        self.driver.get(url)

    def maximize_window(self):
        """Maximize the browser window."""
        self.driver.maximize_window()

    def click_appointment(self):
        """Click the 'Make Appointment' button."""
        self.driver.find_element(*self.appointment_click).click()

    def enter_username(self, username):
        """Enter the username."""
        self.driver.find_element(*self.username_textbox).send_keys(username)

    def enter_password(self, password):
        """Enter the password."""
        self.driver.find_element(*self.password_textbox).send_keys(password)

    def click_login(self):
        """Click the 'Login' button."""
        self.driver.find_element(*self.login_button).click()
