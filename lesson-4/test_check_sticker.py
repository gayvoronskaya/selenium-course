import pytest

from selenium import webdriver


@pytest.fixture()
def set_driver(request):
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    request.addfinalizer(driver.quit)
    return driver

@pytest.mark.test4
def test_check_stickers(set_driver):
    driver = set_driver
    url = "http://localhost/en/"
    driver.get(url)
    products = driver.find_elements_by_xpath("//li[contains(@class,'product column')]")

    for product in products:
        sticker = product.find_elements_by_xpath(
            ".//div[contains(@class,'sticker')]")
        assert len(sticker) == 1
