"""
This module contains account creating page,
the page object for the Automation Test Store - creating account.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage:

    # URLS

    URL = 'https://automationteststore.com/index.php?rt=account/login'

    # Locators

    register_account_button = (By.XPATH, "//button[@title='Continue']")

    # Initializer

    def __init__(self, browser):
        self.browser = browser

    def expected_url(self) -> str:
        return self.URL

    def click_create_account_button(self, ):
        button = self.browser.find_element(*self.register_account_button)
        button.click()
        pass
