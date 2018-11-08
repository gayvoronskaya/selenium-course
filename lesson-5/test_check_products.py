import pytest

from selenium import webdriver


@pytest.fixture()
def set_driver(request):
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    request.addfinalizer(driver.quit)
    return driver


@pytest.mark.test6
def test_check_countries(set_driver):
    driver = set_driver
    url = "http://localhost/en/"
    driver.get(url)
    assert driver.find_element_by_xpath('//div[contains (@id, "logotype")]').is_displayed()

    main_product = driver.find_element_by_xpath('//div[@id="box-campaigns"]//li/a')
    regular_price = main_product.find_element_by_xpath('.//div[@class="price-wrapper"]/s')
    campaign_price = main_product.find_element_by_xpath('.//div[@class="price-wrapper"]/strong')

    main_name = main_product.get_attribute('title')
    main_rp = regular_price.text
    main_cp = campaign_price.text

    mm = regular_price.value_of_css_prorerty('color')
    print(mm)

    main_product.click()


    regular_price = driver.find_element_by_xpath(
        '//div[@class="price-wrapper"]/s')
    campaign_price = driver.find_element_by_xpath(
        '//div[@class="price-wrapper"]/strong')

    detal_rp = regular_price.text
    detal_cp = campaign_price.text
    detal_name = driver.find_element_by_xpath("//h1").text

    assert main_name == detal_name
    assert main_rp == detal_rp
    assert main_cp == detal_cp