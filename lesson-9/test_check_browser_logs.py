import pytest

from selenium import webdriver

@pytest.fixture()
def set_driver(request):
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    request.addfinalizer(driver.quit)
    return driver

def test_login(set_driver):
    driver = set_driver
    url = "http://localhost/admin/"
    driver.get(url)
    driver.find_element_by_xpath('//input[@name="username"]').send_keys("admin")
    driver.find_element_by_xpath('//input[@name="password"]').send_keys("admin")
    driver.find_element_by_xpath('//button[@name="login"]').click()
    assert driver.find_element_by_xpath('//div[@class="logotype"]').is_enabled()

@pytest.mark.test11
def test_browser_logs(set_driver):
    driver = set_driver
    test_login(driver)
    catalog = driver.find_element_by_xpath('//span[text()="Catalog"]')
    catalog.click()
    rubber_ducks = driver.find_element_by_xpath('//a[text() = "Rubber Ducks"]')
    rubber_ducks.click()
    products = driver.find_elements_by_xpath(
        '//td/img//following::a[not(@title="Edit")]')

    i = 0
    errlog = []
    while i < len(products):
        products = driver.find_elements_by_xpath(
            '//td/img//following::a[not(@title="Edit")]')
        products[i].click()
        error = driver.get_log("driver")
        if error:
            for i in error:
                errlog.append(i)
        driver.back()
        i +=1

    assert not errlog
