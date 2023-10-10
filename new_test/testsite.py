from BaseApp import BasePage
from selenium.webdriver.common.by import By


class TestSearchLocators:
    LOCATOR_LOGIN_FIELD = (By.XPATH, """//*[@id="login"]/div[1]/label """)
    LOCATOR_PASS_FIELD = (By.XPATH, """//*[@id="login"]/div[2]/label/input """)
    LOCATOR_ERROR_FIELD = (By.XPATH, """//*[@id="app"]/main/div/div/div[2]/h2""")
    LOCATOR_LOGIN_BTN = (By.CSS_SELECTOR, "button")
    LOCATOR_LOGIN_NAME = (By.XPATH, """//*[@id="app"]/main/nav/ul/li[3]/a""")
    LOCATOR_CREATE_POST_BTN = (By.XPATH, """//*[@id="create-btn"]""")
    LOCATOR_ADD_TITLE = (By.XPATH, """//*[@id="create-item"]/div/div/div[1]/div/label/input""")
    LOCATOR_ADD_DESCRIPTION = (By.XPATH, """//*[@id="create-item"]/div/div/div[2]/div/label/span/textarea""")
    LOCATOR_ADD_CONTENT = (By.XPATH, """//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea""")
    LOCATOR_SAVE_POST_BTN = (By.XPATH, """//*[@id="create-item"]/div/div/div[7]/div/button/span""")
    LOCATOR_CREATE_POST_CHECK = (By.XPATH, """//*[@id="app"]/main/div/div[1]/h1""")
    LOCATOR_CONTACT_US_BTN = (By.XPATH,"""//*[@id="app"]/main/nav/ul/li[2]/a""")
    LOCATOR_CONTACT_US_TEXT = (By.XPATH, """//*[@id="app"]/main/div/div/h1""")
    LOCATOR_YOUR_NAME_FIELD = (By.XPATH, """//*[@id="contact"]/div[1]/label/input""")
    LOCATOR_YOUR_EMAIL_FIELD = (By.XPATH, """//*[@id="contact"]/div[2]/label/input""")
    LOCATOR_CONTENT_IN_CONTACT_FIELD = (By.XPATH, """//*[@id="contact"]/div[3]/label/span/textarea""")
    LOCATOR_ADD_CONTACT_BTN = (By.XPATH, """//*[@id="contact"]/div[4]/button/div""")


class OperationHelper(BasePage):
    def enter_login(self, word):
        login_field = self.find_element(TestSearchLocators.LOCATOR_LOGIN_FIELD)
        # login_field.clear()
        login_field.send_keys(word)

    def enter_pass(self, word):
        login_field = self.find_element(TestSearchLocators.LOCATOR_PASS_FIELD)
        # login_field.clear()
        login_field.send_keys(word)

    def click_login_button(self):
        self.find_element(TestSearchLocators.LOCATOR_LOGIN_BTN).click()

    def get_error_text(self):
        error_field = self.find_element(TestSearchLocators.LOCATOR_ERROR_FIELD, time=3)
        return error_field.text

    def click_new_post_button(self):
        self.find_element(TestSearchLocators.LOCATOR_CREATE_POST_BTN).click()

    def add_title(self, text):
        title_field = self.find_element(TestSearchLocators.LOCATOR_ADD_TITLE)
        title_field.send_keys(text)

    def add_description(self, text):
        description_field = self.find_element(TestSearchLocators.LOCATOR_ADD_DESCRIPTION)
        description_field.send_keys(text)

    def add_content(self, text):
        content_field = self.find_element(TestSearchLocators.LOCATOR_ADD_CONTENT)
        content_field.send_keys(text)

    def click_save_post_button(self):
        self.find_element(TestSearchLocators.LOCATOR_SAVE_POST_BTN).click()

    def get_login_name_text(self):
        login_name_field = self.find_element(TestSearchLocators.LOCATOR_LOGIN_NAME, time=3)
        return login_name_field.text

    def get_post_title_text(self):
        post_title_field = self.find_element(TestSearchLocators.LOCATOR_CREATE_POST_CHECK, time=10)
        return post_title_field.text

    def go_to_contact(self):
        self.find_element(TestSearchLocators.LOCATOR_CONTACT_US_BTN).click()

    def get_contact_us_text(self):
        contact_text = self.find_element(TestSearchLocators.LOCATOR_CONTACT_US_TEXT, time=5)
        return contact_text.text

    def enter_contact_name(self, name):
        contact_name = self.find_element(TestSearchLocators.LOCATOR_YOUR_NAME_FIELD)
        contact_name.send_keys(name)

    def enter_contact_email(self, email):
        contact_email = self.find_element(TestSearchLocators.LOCATOR_YOUR_EMAIL_FIELD)
        contact_email.send_keys(email)

    def enter_content_in_contact(self, text):
        content = self.find_element(TestSearchLocators.LOCATOR_CONTENT_IN_CONTACT_FIELD)
        content.send_keys(text)

    def click_contact_us_button(self):
        self.find_element(TestSearchLocators.LOCATOR_ADD_CONTACT_BTN).click()

    def get_alert_text(self):
        alert = self.driver.switch_to_alert
        return alert.text




