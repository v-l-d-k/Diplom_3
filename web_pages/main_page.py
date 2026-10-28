import allure
from web_locators.locators import MainPageLocators, OrdersPageLocators
from web_pages import BasePage


class MainPage(BasePage):

    @allure.step('Переход на страницу Лента заказов')
    def click_orders_list_button(self):
        self.wait_for_element_to_be_clickable(MainPageLocators.ORDERS_LIST_BUTTON)
        self.click_element_js(MainPageLocators.ORDERS_LIST_BUTTON)
        self.wait_until_element_visibility(OrdersPageLocators.ORDERS_LIST_TITLE)

    @allure.step('Переход в "Конструктор"')
    def click_constructor_button(self):
        self.click_on_element(MainPageLocators.CONSTRUCTOR_BUTTON)
        self.wait_until_element_visibility(MainPageLocators.MAIN_LIST_TITLE)

    @allure.step('Кликаем на ингредиент')
    def click_on_ingredient(self):
        self.wait_for_element_to_be_clickable(MainPageLocators.BUN_INGREDIENT)
        self.click_on_element(MainPageLocators.BUN_INGREDIENT)

    @allure.step('Проверяем, что появилось всплывающее окно с деталями игридиента')
    def check_show_window_with_details(self):
        self.wait_until_element_visibility(MainPageLocators.INGREDIENT_DETAILS_POPUP)
        return self.get_actually_text(MainPageLocators.INGREDIENT_DETAILS_POPUP)

    @allure.step('Закрываем попап крестиком')
    def click_cross_button(self):
        self.move_to_element_and_click(MainPageLocators.CROSS_BUTTON)

    @allure.step('Проверить скрытость деталей ингредиентов')
    def invisibility_ingredient_details(self):
        self.check_invisibility(MainPageLocators.INGREDIENT_DETAILS_POPUP)

    @allure.step('Проверить наличие деталей ингредиентов на экране')
    def check_displayed_ingredient_details(self) -> bool:
        return self.check_presense(MainPageLocators.INGREDIENT_DETAILS_POPUP).is_displayed()

    @allure.step('Получаем значение счетчика ингредиента')
    def get_count_value(self):
        return self.get_actually_text(MainPageLocators.INGREDIENT_COUNTER)

    @allure.step('Добавить ингридиент в заказ')
    def add_filling_to_order(self):
        self.wait_for_element_to_be_clickable(MainPageLocators.BUN_INGREDIENT)
        self.drag_and_drop_on_element(MainPageLocators.BUN_INGREDIENT, MainPageLocators.ORDER_BASKET)

    @allure.step('Нажать на кнопку Оформить заказ')
    def click_order_button(self):
        self.move_to_element_and_click(MainPageLocators.CREATE_ORDER_BUTTON)

    @allure.step('Получение ORDER_ID')
    def get_with_order_id(self):
        self.wait_until_element_visibility(MainPageLocators.ORDER_IDENTIFICATE)
        order_id = self.get_actually_text(MainPageLocators.ORDER_ID)
        while order_id == '9999':
            order_id = self.get_actually_text(MainPageLocators.ORDER_ID)
        return f"{order_id}"

    @allure.step("Закрыть модальное окно после создания заказа")
    def click_close_modal_order(self):
        self.wait_until_element_visibility(MainPageLocators.CLOSE_MODAL_ORDER)
        self.click_element_js(MainPageLocators.CLOSE_MODAL_ORDER)
        self.check_invisibility(MainPageLocators.ORDER_IDENTIFICATE)