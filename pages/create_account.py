"""
This module contains account creating page,
the page object for the Automation Test Store - creating account.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from faker import Faker
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class CreateAccountPage:

    # URLS

    URL = 'https://automationteststore.com/index.php?rt=account/create'
    success_URL = 'https://automationteststore.com/index.php?rt=account/success'

    # Locators

    fake = Faker()

    account_create_firstname = (By.ID, 'AccountFrm_firstname')
    account_create_lastname = (By.ID, 'AccountFrm_lastname')
    account_create_email = (By.ID, 'AccountFrm_email')
    account_create_telephone = (By.ID, 'AccountFrm_telephone')
    account_create_fax = (By.ID, 'AccountFrm_fax')
    account_create_company = (By.ID, 'AccountFrm_company')
    account_create_address_1 = (By.ID, 'AccountFrm_address_1')
    account_create_address_2 = (By.ID, 'AccountFrm_address_2')
    account_create_city = (By.ID, 'AccountFrm_city')
    account_create_zone_id = (By.ID, 'AccountFrm_zone_id')
    account_create_postcode = (By.ID, 'AccountFrm_postcode')
    account_create_country_id = (By.ID, 'AccountFrm_country_id')
    account_create_loginname = (By.ID, 'AccountFrm_loginname')
    account_create_password = (By.ID, 'AccountFrm_password')
    account_create_confirm = (By.ID, 'AccountFrm_confirm')
    account_create_newsletter0 = (By.ID, 'AccountFrm_newsletter0')
    account_create_AccountFrm_agree = (By.ID, 'AccountFrm_agree')
    account_create_Continue_button = (By.XPATH, "//button[@title='Continue']")

    # Initializer

    def __init__(self, browser):
        self.browser = browser

    def expected_url(self) -> str:
        return self.URL

    def type_in_form(self, locator, content):
        form = self.browser.find_element(*locator)
        form.send_keys(content)
        pass

    def wait_for_element_to_load(self, locator,  time: int = 10):
        wait = WebDriverWait(self.browser, time)
        wait.until(expected_conditions.visibility_of_element_located(locator))

    def dropdown_selection_text(self, locator, selection):
        self.wait_for_element_to_load(locator)
        dropdown_menu = Select(self.browser.find_element(*locator))
        dropdown_menu.select_by_visible_text(selection)
        pass

    def dropdown_selection_1st_option(self, locator):
        self.wait_for_element_to_load(locator)
        dropdown_menu = Select(self.browser.find_element(*locator))
        dropdown_menu.select_by_index(1)
        pass

    def click(self, locator):
        self.wait_for_element_to_load(locator)
        point = self.browser.find_element(*locator)
        point.click()
        pass

    def fill_in_form(self):
        self.type_in_form(self.account_create_firstname, self.fake.first_name())
        self.type_in_form(self.account_create_lastname, self.fake.last_name())
        self.type_in_form(self.account_create_email, self.fake.email())
        self.type_in_form(self.account_create_address_1, self.fake.address())
        self.type_in_form(self.account_create_postcode, self.fake.zipcode())
        self.type_in_form(self.account_create_loginname, self.fake.user_name())
        pw = self.fake.password()
        self.type_in_form(self.account_create_password, pw)
        self.type_in_form(self.account_create_confirm, pw)
        self.dropdown_selection_text(self.account_create_country_id, self.fake.country())
        self.dropdown_selection_1st_option(self.account_create_zone_id)
        self.click(self.account_create_newsletter0)
        self.click(self.account_create_AccountFrm_agree)

        pass

    def click_continue_button(self):
        self.click(self.account_create_Continue_button)


