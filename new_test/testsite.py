import logging
import time
import yaml

from BaseApp import BasePage
from selenium.webdriver.common.by import By


class TestSearchLocators:
    ids = dict()
    with open("locators.yaml") as f:
        locators = yaml.safe_load(f)
    for locator in locators["xpath"].keys():
        ids[locator] = (By.XPATH, locators["xpath"][locator])
    for locator in locators["css"].keys():
        ids[locator] = (By.CSS_SELECTOR, locators["css"][locator])


class OperationHelper(BasePage):
    def enter_text_into_field(self, locator, word, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        logging.debug(f"Send {word} to element {element_name}")
        field = self.find_element(locator)
        if not field:
            logging.error(f"Element {locator} not found")
            return False
        try:
            # field.clear()
            field.send_keys(word)
        except:
            logging.exception(f"Exeption while operation with {locator}")
            return False
        return True

    def click_button(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        button = self.find_element(locator)
        if not button:
            return False
        try:
            button.click()
        except:
            logging.exception("Exeption with click")
            return False
        logging.debug(f"Clicked {element_name} button")
        return True

    def get_text_from_element(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        field = self.find_element(locator, time=3)
        if not field:
            return None
        try:
            text = field.text
        except:
            logging.exception(f"Exeption while get text from {element_name}")
            return None
        logging.debug(f"We find text {text} in field {element_name}")
        return text

    # ENTER TEXT
    def enter_login(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_LOGIN_FIELD"], word, description="login form")

    def enter_pass(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_PASS_FIELD"], word, description="password form")

    def add_title(self, text):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_ADD_TITLE"], text, description="title form")

    def add_description(self, text):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_ADD_DESCRIPTION"], text,
                                   description="description form")

    def add_content(self, text):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_ADD_CONTENT"], text, description="content form")

    def enter_contact_name(self, name):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_YOUR_NAME_FIELD"], name, description="name form")

    def enter_contact_email(self, email):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_YOUR_EMAIL_FIELD"], email, description="email form")

    def enter_content_in_contact(self, text):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_CONTENT_IN_CONTACT_FIELD"], text,
                                   description="content form")

    # CLICK

    def click_login_button(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_LOGIN_BTN"], description="login")

    def click_new_post_button(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_CREATE_POST_BTN"], description="create post")

    def click_save_post_button(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_SAVE_POST_BTN"], description="save post")

    def click_contact_us_button(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_ADD_CONTACT_BTN"], description="contact us")
        time.sleep(1)
        alert = self.driver.switch_to.alert
        return alert.text

    def go_to_contact(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_CONTACT_US_BTN"], description="go to contact us page")

    # GET TEXT
    def get_error_text(self):
        return self.get_text_from_element(TestSearchLocators.ids["LOCATOR_ERROR_FIELD"])

    def get_login_name_text(self):
        return self.get_text_from_element(TestSearchLocators.ids["LOCATOR_LOGIN_NAME"])

    def get_post_title_text(self):
        return self.get_text_from_element(TestSearchLocators.ids["LOCATOR_CREATE_POST_CHECK"])

    def get_contact_us_text(self):
        return self.get_text_from_element(TestSearchLocators.ids["LOCATOR_CONTACT_US_TEXT"])
