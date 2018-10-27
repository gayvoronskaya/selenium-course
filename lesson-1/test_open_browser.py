import pytest
from selenium import webdriver


@pytest.fixture()
def set_driver(request):
    driver = webdriver.Chrome()
    request.addfinalizer(driver.quit)
    return driver


@pytest.mark.test1
def test_open_browser(set_driver):
    driver = set_driver
    url = "https://yandex.ru"
    driver.get(url)
