from selenium.webdriver.common.by import By
from pages.base_page import Page



class Header(Page):
    TOP_LOGO_LINK = (By.CSS_SELECTOR, "a.header__heading-link")
    CART_LINK = (By.CSS_SELECTOR, "span#cart-icon-bubble")


    def click_cart(self):
        self.click(*self.CART_LINK)


    def top_logo(self):
        self.click(*self.TOP_LOGO_LINK)