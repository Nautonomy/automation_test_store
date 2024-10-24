"""
This module contains Homepage,
the page object for the Automation Test Store homepage.

"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Homepage:
    # URLS

    URL = 'https://automationteststore.com/'

    # Locators

    account_link = (By.LINK_TEXT, 'Login or register')

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)
        pass

    def click_account_link(self):
        button = self.browser.find_element(*self.account_link)
        button.click()
        pass