from constants.selectors import Search
from constants.selectors import Filter
from constants.selectors import Footer
from base import Base
from selenium.webdriver.common.keys import Keys


class SearchPage(Base):

    def search_for_product(self, product_name):
        self.wait_for_elements(Search.search_FIELD)
        self.send_keys_to_the_element(Search.search_FIELD, product_name)
        self.send_keys_to_the_element(Search.search_FIELD, Keys.RETURN)

    def get_price_from_product(self):
        self.wait_for_elements(Search.price_from_product)
        return self.get_text_from_element(Search.price_from_product)

    def enter_min_price(self, price):
        self.wait_for_elements(Filter.min_INPUT)
        self.send_keys_to_the_element(Filter.min_INPUT, price)

    def enter_max_price(self, price):
        self.wait_for_elements(Filter.max_INPUT)
        self.send_keys_to_the_element(Filter.max_INPUT, price)

    def submit_range_filter(self):
        self.wait_for_elements(Filter.search_range_BTN)
        self.click_on_element(Filter.search_range_BTN)

    def select_currency(self, currency):
        self.wait_for_elements(Footer.currency_SELECT)
        self.click_on_element(Footer.currency_SELECT)
        self.click_on_element(Footer.currency_test % currency)

    def select_sort_by_price(self, type_sort):
        self.wait_for_elements(Filter.sort_price_SELECT)
        self.select_by_value(Filter.sort_price_SELECT, type_sort)
