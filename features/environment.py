from time import sleep
import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
#from selenium.webdriver.firefox.service import Service
#from selenium.webdriver.firefox.options import Options


from app.application import Application



def browser_init(context):
    """
    :param context: Behave context
    """

    service = Service(executable_path=r'C:\Users\brown\CureskinProject\chromedriver-win64')
    context.driver = webdriver.Chrome(service=service)

    #driver_path = ChromeDriverManager().install()
    #service = Service(driver_path)
    #options = webdriver.ChromeOptions()
    #options.add_argument('--headless')
    #context.driver = webdriver.Chrome(chrome_options=options,service=service)

    #context.driver = webdriver.Firefox(executable_path=r'C:\Users\brown\CureskinProject\geckodriver')

    #options = Options()
    #options.headless = True
    #driver = webdriver.Firefox(options=options, executable_path=r'C:\Users\brown\CureskinProject\geckodriver')

    #### BROWSERSTACK ####
    #desired_cap = {
    #     'browser': 'Firefox',
    #     'os_version': '11',
    #     'os': 'Windows',
    #     'name': logo_link
    #  }
    #bs_user = 'dalupack_lC9aX5'
    #bs_key = 'HyyVRiy67szwWJtuxTbE'
    #url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    #context.driver = webdriver.Remote(url, desired_capabilities=desired_cap)


    #behave -f allure_behave.formatter:AllureFormatter -o test_results/features/tests/link_verification.feature


    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, 10)

    context.app = Application(context.driver)

def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.delete_all_cookies()
    context.quit()
