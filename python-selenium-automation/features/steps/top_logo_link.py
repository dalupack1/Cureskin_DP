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


@given("Open Cureskin main page")
def open_cureskin_main_page(context):
    context.driver.get('https://shop.cureskin.com/')


@when("Click on cart")
def click_cart(context):
    context.driver.find_element(*CART_LINK).click()


@when("Click on logo")
def click_top_logo(context):
    context.driver.find_element(*TOP_LOGO_LINK).click()


@then("Verify user is on homepage")
def homepage_verification(context):
    context.driver.wait.until(EC.url_to_be('https://shop.cureskin.com/'))