from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait

TOP_LOGO_LINK = (By.CSS_SELECTOR, "a.header__heading-link")
CART_LINK = (By.CSS_SELECTOR, "span#cart-icon-bubble")


@given("Open search results page")
def open_search_results_page(context):
    context.app.Search_results_page.open_search_results_page()


@when("Click on Cureskin logo")
def click_top_logo(context):
    context.app.Header.top_logo()


@then("Verify user is on homepage")
def homepage_verification(context):
    context.app.Mainpage.homepage_verification()