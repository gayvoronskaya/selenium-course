import pytest

from selenium import webdriver



@pytest.fixture()
def set_driver(request):
    driver = webdriver.Chrome()
    request.addfinalizer(driver.quit)
    return driver


@pytest.mark.test2
def test_login(set_driver):
    driver = set_driver
    url = "http://localhost/admin/"
    driver.get(url)
    driver.find_element_by_xpath('//input[@name="username"]').send_keys("admin")
    driver.find_element_by_xpath('//input[@name="password"]').send_keys("admin")
    driver.find_element_by_xpath('//button[@name="login"]').click()
    assert driver.find_element_by_xpath('//div[@class="logotype"]').is_enabled()
