from web_pages.auth_user_page import AuthUserPage
from web_pages.base_page import BasePage
from web_pages.main_page import MainPage
from web_pages.create_order_page import CreateOrderPage


class UIWorkerWeb(MainPage, AuthUserPage, CreateOrderPage):
    """Класс объединяет все классы по работе со страницами используя множественное наследование"""
    def __init__(self, driver, locators):
        super().__init__(driver)
        self.locators = locators