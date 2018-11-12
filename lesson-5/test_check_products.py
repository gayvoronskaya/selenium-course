import pytest
import re

from selenium import webdriver


@pytest.fixture()
def set_driver(request):
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    request.addfinalizer(driver.quit)

    return driver

def get_rgba(rgba_pattern, raw_css_value):
    rgba_elements_count = 4
    raw_rgba = rgba_pattern.search(raw_css_value).groups()
    if len(raw_rgba) != rgba_elements_count:
        raise Exception("incorrect rgba value: %s" % raw_css_value)

    return tuple(map(int, raw_rgba))

def is_red(rgba_color):
    return rgba_color[1] is 0 and rgba_color[2] is 0

def is_gray(rgba_color):
    return rgba_color[0] == rgba_color[1] == rgba_color[2]

@pytest.mark.test6
def test_check_countries(set_driver):
    rgba_pattern = re.compile(
        r'rgba\((\d{1,3}),\s+(\d{1,3}),\s+(\d{1,3}),\s+(\d|\d\.\d+)\)')

    driver = set_driver
    url = "http://localhost/en/"
    driver.get(url)
    assert driver.find_element_by_xpath(
        '//div[contains (@id, "logotype")]').is_displayed()

    main_product = driver.find_element_by_xpath(
        '//div[@id="box-campaigns"]//li/a')
    regular_price = main_product.find_element_by_xpath(
        './/div[@class="price-wrapper"]/s')
    campaign_price = main_product.find_element_by_xpath(
        './/div[@class="price-wrapper"]/strong')

    main_name = main_product.get_attribute('title')
    main_rp = regular_price.text
    main_cp = campaign_price.text

    color_main_rp = regular_price.value_of_css_property('color')
    color_main_cp = campaign_price.value_of_css_property('color')
    size_main_rp = float(
        regular_price.value_of_css_property('font-size').replace('px', ''))
    size_main_cp = float(
        campaign_price.value_of_css_property('font-size').replace('px', ''))

    assert is_gray(get_rgba(rgba_pattern,color_main_rp))
    assert is_red(get_rgba(rgba_pattern, color_main_cp))
    assert size_main_cp > size_main_rp

    main_product.click()

    regular_price = driver.find_element_by_xpath(
        '//div[@class="price-wrapper"]/s')
    campaign_price = driver.find_element_by_xpath(
        '//div[@class="price-wrapper"]/strong')

    detail_name = driver.find_element_by_xpath("//h1").text
    detail_rp = regular_price.text
    detail_cp = campaign_price.text
    color_detail_rp = regular_price.value_of_css_property('color')
    color_detail_cp = campaign_price.value_of_css_property('color')
    size_detail_rp = float(
        regular_price.value_of_css_property('font-size').replace('px', ''))
    size_detail_cp = float(
        campaign_price.value_of_css_property('font-size').replace('px', ''))

    assert is_gray(get_rgba(rgba_pattern,color_detail_rp))
    assert is_red(get_rgba(rgba_pattern, color_detail_cp))
    assert size_detail_cp > size_detail_rp

    assert main_name == detail_name
    assert main_rp == detail_rp
    assert main_cp == detail_cp
