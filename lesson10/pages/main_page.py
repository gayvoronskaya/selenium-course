from selenium.webdriver.support.wait import WebDriverWait
from lesson10.pages.product_page import ProductPage


class MainPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get("http://localhost/en/")
        return self

    def click_to_product(self, i):
        products = self.driver.find_elements_by_xpath(
        "//li[contains(@class,'product column')]")
        products[i].click()
        return ProductPage
