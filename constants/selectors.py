class Search(object):
    search_FIELD = "#autocomplete-input"
    price_from_product = "//span[@data-testid='component-price-regular']"


class Filter(object):
    min_INPUT = "//input[@class='ais-RangeInput-inputMin']"
    max_INPUT = "//input[@class='ais-RangeInput-inputMax']"
    search_range_BTN = "//button[@class='ais-RangeInput-submit']"
    sort_price_SELECT = "//select[@class='ais-SortBy-select']"


class Footer():
    currency_SELECT = "//div[@id='mui-component-select-currency']"
    currency_test = "//ul/li[@data-value='%s']"
