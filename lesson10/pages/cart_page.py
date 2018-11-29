from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find_count_products(self):
        count_products_in_cart = self.driver.find_elements_by_xpath(
            '//td[@class="item"]')
        return len(count_products_in_cart)

    def get_product_name(self):
        product_name = self.driver.find_element_by_xpath('//li//strong').text
        return product_name

    def get_product_in_table(self):
        table_product_name = self.driver.find_element_by_xpath(
            '//td[text() = "%s"]' % self.get_product_name())
        return table_product_name

    def remove_product(self):
        remove_button = self.driver.find_element_by_xpath(
            '//button[@name="remove_cart_item"]')
        remove_button.click()

    def wait_delete_from_table(self):
        WebDriverWait(self.driver, 10).until(
            EC.staleness_of(self.get_product_in_table()))

    def is_empty_cart(self):
        warning = self.driver.find_element_by_xpath('//em').text
        return warning == "There are no items in your cart."
