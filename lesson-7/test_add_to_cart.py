import pytest
import time

from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException


@pytest.fixture()
def set_driver(request):
    driver = webdriver.Chrome()
    driver.implicitly_wait(2)
    request.addfinalizer(driver.quit)
    return driver

@pytest.mark.test9
def test_add_product_to_cart(set_driver):
    driver = set_driver
    url = "http://localhost/en/"
    driver.get(url)
    add_to_cart(driver, items=3)

    cart = driver.find_element_by_xpath('//a[text()="Checkout »"]')
    cart.click()

    count_products_in_cart = driver.find_elements_by_xpath('//td[@class="item"]')

    i =1
    while i <= len(count_products_in_cart):
        remove_button = driver.find_element_by_xpath('//button[@name="remove_cart_item"]')
        remove_button.click()
        WebDriverWait(driver, 10).until(
            lambda d, : d.find_elements_by_xpath(
                '//td[@class="item"]'))
        count_products_in_cart = driver.find_elements_by_xpath(
            '//td[@class="item"]')
        print(len(count_products_in_cart))
        i +=1


    time.sleep(10)


def add_to_cart(driver, items):

    i = 1
    while i <= items:

        products = driver.find_elements_by_xpath(
            "//li[contains(@class,'product column')]")
        products[0].click()

        try:
            select_size = Select(driver.find_element_by_xpath(
                '//select[@name="options[Size]"]'))
            select_size.select_by_value("Medium")
        except NoSuchElementException:
            pass

        button_add_to_cart = driver.find_element_by_xpath(
            '//button[@name="add_cart_product"]')
        button_add_to_cart.click()

        WebDriverWait(driver, 10).until(
            lambda d, x=i: d.find_element_by_xpath(
                '//span[@class="quantity" and text()=%s]' % x))

        logotype_link = driver.find_element_by_xpath(
            '//div[@id="logotype-wrapper"]/a')
        logotype_link.click()
        i += 1
