import pytest
import string
import random

from selenium import webdriver
from selenium.webdriver.support.select import Select


@pytest.fixture()
def set_driver(request):
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    request.addfinalizer(driver.quit)
    return driver


@pytest.mark.test7
def test_registration(set_driver):

    first_name = "Anastasiya"
    last_name = "Gayvoronskaya"
    city = "Miami"
    phone = "+15555555555"
    password = "123123"
    address = "NW 14th St"

    driver = set_driver
    url = "http://localhost/en/"
    driver.get(url)

    sign_up = driver.find_element_by_xpath('//form[@name="login_form"]//a')
    sign_up.click()

    first_name_field = driver.find_element_by_xpath('//input[@name="firstname"]')
    first_name_field.send_keys(first_name)

    last_name_field = driver.find_element_by_xpath('//input[@name="lastname"]')
    last_name_field.send_keys(last_name)

    address1 = driver.find_element_by_xpath('//input[@name="address1"]')
    address1.send_keys(address)

    post_code = driver.find_element_by_xpath('//input[@name="postcode"]')
    post_code.send_keys(get_random_string(size=5, chars=string.digits))

    city_field = driver.find_element_by_xpath('//input[@name="city"]')
    city_field.send_keys(city)

    select_country = Select(driver.find_element_by_xpath(
        '//select[@name="country_code"]'))
    select_country.select_by_visible_text("United States")

    select_state = Select(driver.find_element_by_xpath(
        '//select[@name="zone_code"]'))
    select_state.select_by_visible_text("Florida")

    email_field = driver.find_element_by_xpath('//input[@name="email"]')
    email = ('%s@example.local' %get_random_string())
    email_field.send_keys(email)

    phone_field = driver.find_element_by_xpath('//input[@name="phone"]')
    phone_field.send_keys(phone)

    password_field = driver.find_element_by_xpath('//input[@name="password"]')
    password_field.send_keys(password)

    confirmed_password = driver.find_element_by_xpath(
        '//input[@name="confirmed_password"]')
    confirmed_password.send_keys(password)

    create_account_button = driver.find_element_by_xpath(
        '//button[@name="create_account"]')
    create_account_button.click()

    logout(driver)
    login(driver, email, password)
    logout(driver)

def logout(driver):
    logout_button = driver.find_element_by_xpath('//a[text()="Logout"]')
    logout_button.click()

def login(driver, email, password):
    email_field = driver.find_element_by_xpath('//input[@name="email"]')
    email_field.send_keys(email)
    password_field = driver.find_element_by_xpath('//input[@name="password"]')
    password_field.send_keys(password)
    login_button = driver.find_element_by_xpath('//button[@name="login"]')
    login_button.click()

def get_random_string(size=6, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
