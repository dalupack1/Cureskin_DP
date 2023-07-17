from selenium.webdriver.common.by import By
from pages.base_page import Page


class SearchResultsPage(Page):

    def open_search_results_page(self):
        self.open_url("https://shop.cureskin.com/search?q=cure")