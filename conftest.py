import pytest
from selenium import webdriver

from data.urls import Urls
from web_locators import UIWorkerLocators
from web_pages import UIWorkerWeb


@pytest.fixture(params=['chrome', 'firefox'])
def driver_do(request):
    if request.param == 'chrome':
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        driver = webdriver.Chrome(options=chrome_options)
        driver.set_window_size(1920, 1080)
        driver.get(Urls.BASE_URL + Urls.url_main)
    elif request.param == 'firefox':
        firefox_options = webdriver.FirefoxOptions()
        firefox_options.add_argument('--headless')
        driver = webdriver.Firefox(options=firefox_options)
        driver.set_window_size(1920, 1080)
        driver.get(Urls.BASE_URL + Urls.url_main)
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def pages(driver_do):
    """инициализирует класс с selenium driver"""
    driver = driver_do
    pages = UIWorkerWeb(driver, UIWorkerLocators())
    return pages


@pytest.fixture(scope='function')
def login(pages):
    """ Войти в аккаунт """
    pages.login()