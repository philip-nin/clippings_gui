import lxml.builder
import lxml.etree
import selenium.webdriver.support.expected_conditions as EC
from cssselect import GenericTranslator, SelectorError
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from mapping_asserts import MappingAsserts
from selenium.common.exceptions import TimeoutException

import re
import time
from timeit import default_timer as timer
import logging

log = logging.getLogger('verbose')
log.setLevel(logging.INFO)


class FakeWebdriver(webdriver.Remote):
    def __init__(self):
        pass


class Base(MappingAsserts):
    driver = FakeWebdriver()

    def wait_for_elements(self, selector_value, timeout=10):
        log.info("Starting to wait for element" + selector_value)
        start = timer()
        wait = WebDriverWait(self.driver, timeout)
        test = self.locator(selector_value)
        element = wait.until(EC.visibility_of_element_located((test, selector_value)))
        end = timer()
        wait_time = end - start
        log.info("Waited for element = " + selector_value + " for " + str(wait_time) + " seconds")
        return element

    def wait_for_elements_not_visible(self, selector_value, timeout=10):
        start = timer()
        wait = WebDriverWait(self.driver, timeout)
        test = self.locator(selector_value)
        element = wait.until(EC.invisibility_of_element_located((test, selector_value)))
        end = timer()
        wait_time = end - start
        log.info("Waiting for element NOT visible = " + selector_value + " for " + str(wait_time) + " seconds")
        return element

    def select_by_value(self, locator, value):
        Select(self.find_element(locator)).select_by_value(value)

    def wait_for_text(self, selector_value, text, timeout=10):
        start = timer()
        wait = WebDriverWait(self.driver, timeout)
        test = self.locator(selector_value)
        element = wait.until(EC.text_to_be_present_in_element(test, text))
        end = timer()
        wait_time = end - start
        log.info(
            "Waiting for text: " + text + " in selector = " + selector_value + " for " + str(wait_time) + " seconds")
        return element

    def wait_and_accept_alert(self):
        try:
            wait = WebDriverWait(self.driver, 10)
            wait.until(EC.alert_is_present(), 'There you are')
            self.driver.switch_to.alert.accept()
            #print("Alert text is " + alert.text)
            #alert.accept()
        except TimeoutException:
            print("No alert is shown, continue")


    def check_for_element(self, selector):
        test = self.locator(selector)
        try:
            self.find_element(test)
        except NoSuchElementException:
            return False
        return True

    def find_element(self, locator):
        loc_type = self.locator(locator)
        return self.driver.find_element(loc_type, locator)

    def click_on_element(self, locator):
        log.info("Clicking on element " + locator)
        self.find_element(locator).click()

    def get_text_from_element(self, locator):
        log.info("The element contain data: " + self.find_element(locator).text)
        return self.find_element(locator).text

    def get_value_from_element(self, locator):
        log.info("The element contain data: " + self.find_element(locator).get_attribute('value'))

        return self.find_element(locator).get_attribute('value')

    def send_keys_to_the_element(self, locator, keys):
        log.info("Sending data: " + str(keys) + " to element: " + locator)
        self.find_element(locator).clear()
        self.find_element(locator).send_keys(keys)

    def go_to_bottom(self):
        html = self.find_element("//html")
        html.send_keys(Keys.END)

    def locator(self, locator):
        if self.isCss(locator):
            return By.CSS_SELECTOR
        elif self.isID(locator):
            return By.ID
        elif self.isXpath(locator):
            return By.XPATH
        else:
            return "ERRRORRR"

    def isCss(self, locator):
        try:
            GenericTranslator().css_to_xpath(locator)
        except SelectorError:
            return False
        return True

    def isID(self, id):
        return bool(re.search('~^#[\w\.\-\[\]\=\^\~\:]+$~', id))

    def isXpath(self, locator):
        root = lxml.etree.Element("root")
        try:
            root.xpath(locator)
        except lxml.etree.XPathEvalError:
            return False
        else:
            return True

    def extract_numbers(self, string):
        return re.sub("\D", "", string)

    def get_order_id_from_details(self, string):
        return re.search("#[A-Za-z0-9]*", string).group(0)

    def remove_cents(self, price):
        point = price.find(".")
        cents = price[point + 1:]
        integet = price[:point]
        return int(integet)


    def remove_first_character(self, string):
        return string[1:]

    def price_to_integer(self, price):
        return self.remove_cents(self.remove_first_character(price))

    def hover(self, element):
        wd = self.driver
        element1 = self.find_element(element)
        hov = ActionChains(wd).move_to_element(element1)
        hov.perform()

    def remove_element_from_DOM(self, element_to_remove):
        self.wait_for_elements(element_to_remove)
        time.sleep(2)
        elem = self.find_element(element_to_remove)
        self.driver.execute_script("arguments[0].remove();", elem)

    def click_with_coordinates(self, x=0, y=0):
        el = self.driver.find_element_by_xpath("//body")

        action = webdriver.common.action_chains.ActionChains(self.driver)
        action.move_to_element_with_offset(el, x, y)
        action.click()
        action.perform()

    def get_number_of_inner_elements(self, elem):
        return self.driver.find_elements_by_xpath(elem)


class BaseLoggedIn(Base):
    def setUp(self):
        self.driver.get("https://clippings.com/search")
