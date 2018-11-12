import pytest
import string
import time
import random

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


@pytest.fixture()
def set_driver(request):
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    request.addfinalizer(driver.quit)
    return driver


@pytest.mark.test7
def test_check_countries(set_driver):
    FIRST_NAME = "Anastasiya"
    LAST_NAME = "Gayvoronskaya"
    POSTCODE = "63008"  #TODO рандомную последовательность из 5 чисел сделать
    CITY = "Novosibirsk"
    EMAIL = "ng3003ng@ngs.ru" #TODO сделать рандомный email
    driver = set_driver
    url = "http://localhost/en/"
    driver.get(url)
    sign_up = driver.find_element_by_xpath('//form[@name="login_form"]//a')
    sign_up.click()
    first_name = driver.find_element_by_xpath('//input[@name="firstname"]')
    first_name.send_keys(FIRST_NAME)
    last_name = driver.find_element_by_xpath('//input[@name="lastname"]')
    last_name.send_keys(LAST_NAME)
    address1 = driver.find_element_by_xpath('//input[@name="address1"]')
    address1.send_keys("test1")
    post_code = driver.find_element_by_xpath('//input[@name="postcode"]')
    post_code.send_keys(get_random_string(size=5, chars=string.digits))
    city = driver.find_element_by_xpath('//input[@name="city"]')
    city.send_keys(CITY)
    #TODO сделать выбор любого рандомного штата
    country_selector = driver.find_element_by_xpath('//span[@class="selection"]')
    country_selector.click()
    email = driver.find_element_by_xpath('//input[@name="email"]')
    email.send_keys('%s@example.local' % get_random_string())
    time.sleep(30)

def get_random_string(size=6, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))




