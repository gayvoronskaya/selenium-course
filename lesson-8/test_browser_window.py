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

@pytest.mark.test10
def test_window(set_driver):
    driver = set_driver
    test_login(driver)

    countries = driver.find_element_by_xpath('//span[text()="Countries"]')
    countries.click()

    add_new_country = driver.find_element_by_xpath(
        '//div/a[contains (@href, "edit_country")]')

    add_new_country.click()

    external_links = driver.find_elements_by_xpath(
        '//i[@class="fa fa-external-link"]')

    for link in external_links:
        link.click()
        main_window = driver.current_window_handle
        print("111111" + main_window)
        exciting_windows = driver.window_handles
        print(exciting_windows)


