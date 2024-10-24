"""
These tests cover creating user account.
"""

from pages.homepage import Homepage
from pages.login import LoginPage
from pages.create_account import CreateAccountPage


def test_account_register(browser):
    homepage = Homepage(browser)
    login_page = LoginPage(browser)
    create_account_page = CreateAccountPage(browser)

    # access login page via home page
    homepage.load()
    homepage.click_account_link()
    current_url = browser.current_url
    expected_url1 = login_page.expected_url()
    assert current_url == expected_url1

    # access create account page

    login_page.click_create_account_button()

    # fill in form and continue

    create_account_page.fill_in_form()
    create_account_page.click_continue_button()

    # assert expected URL is reached

    expected_url2 = create_account_page.success_URL
    assert browser.current_url == expected_url2



