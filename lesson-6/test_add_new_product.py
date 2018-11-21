import os
import random

import pytest

from datetime import date
from datetime import timedelta
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


@pytest.fixture()
def set_driver(request):
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    request.addfinalizer(driver.quit)
    return driver

def login_admin(driver):
    url = "http://localhost/admin/"
    driver.get(url)
    driver.find_element_by_xpath('//input[@name="username"]').send_keys("admin")
    driver.find_element_by_xpath('//input[@name="password"]').send_keys("admin")
    driver.find_element_by_xpath('//button[@name="login"]').click()
    assert driver.find_element_by_xpath(
        '//div[@class="logotype"]').is_displayed()

def fill_general_tab(form):
    form_find = form.find_element_by_xpath
    form_finds = form.find_elements_by_xpath

    enabled_button = form_find('.//label[text()=" Enabled"]//input')
    enabled_button.click()

    product_title = "Perfume № %d" % random.randint(1, 100)
    product_name = form_find('.//input[@name="name[en]"]')
    product_name.send_keys(product_title)


    product_code = form_find('.//input[@name="code"]')
    product_code.send_keys(random.randint(100, 1000))

    products_quantity = form_find('.//input[@name="quantity"]')
    products_quantity.clear()
    products_quantity.send_keys(random.randint(10, 100))

    image = form_find('.//input[@type="file"]')
    image.send_keys(os.getcwd() + "/lesson-6/product.jpg")

    for product in form_finds('.//input[@name="product_groups[]"]'):
        product.click()

    date_from = form_find('.//input[@name="date_valid_from"]')
    date_today = date.today()
    date_from.send_keys(date_today.strftime("%m%d%Y"))

    date_to = form_find('.//input[@name="date_valid_to"]')
    date_to.send_keys((date_today + timedelta(days=1)).strftime("%m%d%Y"))

    return product_title

def fill_information_tab(driver, form):
    form_find = form.find_element_by_xpath

    keywords = form_find('.//input[@name="keywords"]')
    wait = WebDriverWait(driver, 5)
    wait.until(EC.visibility_of(keywords))
    keywords.send_keys("Perfume Eau de perfume, France")

    short_description = form_find('.//input[@name="short_description[en]"]')
    short_description.send_keys("Perfume from magic world!")

    description = form_find('.//div[@class="trumbowyg-editor"]')
    description.send_keys(
        "The best perfume from France. It can be the best present for your friend")

    head_title = form_find('.//input[@name="head_title[en]"]')
    head_title.send_keys("Perfume from France")

def fill_prices_tab(driver, form):
    form_find = form.find_element_by_xpath

    purchase_price = form_find('.//input[@name="purchase_price"]')
    wait = WebDriverWait(driver, 5)
    wait.until(EC.visibility_of(purchase_price))
    purchase_price.clear()
    purchase_price.send_keys(random.randint(100, 500))

    purchase_price_select = Select(
        form_find('.//select[@name="purchase_price_currency_code"]'))
    purchase_price_select.select_by_value("EUR")

    price_usd = form_find('.//input[@name="prices[USD]"]')
    price_usd.send_keys(random.randint(100, 500))

    price_eur = form_find('.//input[@name="prices[EUR]"]')
    price_eur.send_keys(random.randint(100, 500))

def create_new_product(driver):
    driver_find = driver.find_element_by_xpath

    general_form = driver_find('//div[@id="tab-general"]')
    product_title = fill_general_tab(general_form)

    tab_information = driver_find('//a[text()="Information"]')
    tab_information.click()

    information_form = driver_find('//div[@id="tab-information"]')
    fill_information_tab(driver, information_form)

    tab_prices = driver_find('//a[text()="Prices"]')
    tab_prices.click()

    prices_form = driver_find('//div[@id="tab-prices"]')
    fill_prices_tab(driver, prices_form)

    return product_title


@pytest.mark.test8
def test_add_new_product(set_driver):
    driver = set_driver

    login_admin(driver)

    driver_find = driver.find_element_by_xpath

    catalog = driver_find('//span[text()="Catalog"]')
    catalog.click()

    new_product = driver_find('//a[@class="button"][2]')
    new_product.click()

    product_name = create_new_product(driver)

    save_button = driver_find('//button[@name="save"]')
    save_button.click()

    done_product = driver_find('//a[text()="%s"]' % product_name)
    assert done_product.is_displayed()
