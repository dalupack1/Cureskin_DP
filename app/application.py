from pages.Header import Header
from pages.Mainpage import MainPage
from pages.Search_results_page import SearchResultsPage
import allure

class Application:

    def __init__(self, driver):
        self.driver = driver

        self.Header = Header(self.driver)
        self.Mainpage = MainPage(self.driver)
        self.Search_results_page = SearchResultsPage(self.driver)