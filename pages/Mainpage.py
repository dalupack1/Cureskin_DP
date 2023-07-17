from pages.base_page import Page
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class MainPage(Page):

    def open_main_page(self):
        self.open_url('https://shop.cureskin.com/')

    def url_contains(self):
        self.wait.until(EC.url_contains('https://shop.cureskin.com/'))

    def homepage_verification(self):
        self.wait.until(EC.url_to_be('https://shop.cureskin.com/'))
