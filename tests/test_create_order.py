import allure
import pytest

from web_locators.locators import OrdersPageLocators


class TestCreateOrder:
    @allure.title('При создании заказа, происходит увеличения значения счетчиков заказов "Выполнено за все время"/"Выполнено за сегодня"')
    @allure.description('Сверяем счетчик заказов "Выполнено за все время" / "Выполнено за сегодня" до создания заказа и после создания заказа '
                        'Счетчик должен увеличиться')
    @pytest.mark.parametrize('counter', [OrdersPageLocators.TOTAL_ORDER_COUNT, OrdersPageLocators.DAILY_ORDER_COUNT])
    def test_today_orders_counter(self, pages, login, counter):
        pages.click_orders_list_button()
        prev_counter_value = pages.get_total_order_count_daily(counter)
        pages.click_constructor_button()
        pages.add_filling_to_order()
        pages.click_order_button()
        pages.click_close_modal_order()
        pages.click_orders_list_button()
        current_counter_value = pages.get_total_order_count_daily(counter)
        assert current_counter_value > prev_counter_value, "Заказ не создался, counter не сработал"

    @allure.title('Проверка отображения номера заказа в разделе "В работе')
    @allure.description('Получаем номер нового заказа, и проверяем, что номер заказа появился в разделе "В работе"')
    def test_new_order_appears_in_work_list(self, pages, login):
        pages.add_filling_to_order()
        pages.click_order_button()
        order_number = pages.get_with_order_id()
        pages.click_close_modal_order()
        pages.click_orders_list_button()
        order_number_refactor = pages.get_user_order(order_number)
        order_in_progress = pages.get_user_order_in_progress()
        assert order_number_refactor == order_in_progress