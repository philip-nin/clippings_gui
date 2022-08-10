from __future__ import absolute_import
from base import BaseLoggedIn
from pages.searchpage import SearchPage


class TestClippings(BaseLoggedIn, SearchPage):
    def test_min_max_filter(self):
        self.setUp()
        self.search_for_product("como")  #sc53
        price = self.get_price_from_product()
        original_price = self.price_to_integer(price)
        self.enter_min_price(original_price)
        self.enter_max_price(original_price + 1)
        self.submit_range_filter()
        price_using_filter = self.get_price_from_product()
        filtered_price = self.price_to_integer(price_using_filter)

        self.assertEqual(original_price, filtered_price)

    def test_min_max_interval_of_products(self):
        self.setUp()
        self.select_currency("EUR")
        self.enter_min_price(10)
        self.enter_max_price(100)
        self.submit_range_filter()
        self.select_sort_by_price("prod_products_price_desc")  # Price (Highest first)
        price_high = self.get_price_from_product()
        price_high = self.price_to_integer(price_high)
        self.assertTrue(10 <= price_high <= 100)
        self.select_sort_by_price("prod_products_price_asc")  # Price (Lowest first)
        price_low = self.get_price_from_product()
        price_low = self.price_to_integer(price_low)
        self.assertTrue(10 <= price_low <= 100)









