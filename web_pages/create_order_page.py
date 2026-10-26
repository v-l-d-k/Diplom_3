import allure

from web_locators import OrdersPageLocators
from web_pages import BasePage


class CreateOrderPage(BasePage):

    @allure.step("Получение количества заказов")
    def get_total_order_count_daily(self, locator):
        return self.get_actually_text(locator)

    @allure.step('Получаем номер заказа')
    def get_user_order(self, orders_numbers):
        order_refactor = f'0{orders_numbers}'
        self.wait_for_text_to_be_present_in_element(OrdersPageLocators.NUMBER_IN_PROGRESS, order_refactor)
        return order_refactor

    @allure.step('Получаем номер заказа в работе')
    def get_user_order_in_progress(self):
        return self.get_actually_text(OrdersPageLocators.NUMBER_IN_PROGRESS)