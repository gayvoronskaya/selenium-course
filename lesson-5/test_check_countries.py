import pytest

from selenium import webdriver


@pytest.fixture()
def set_driver(request):
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    request.addfinalizer(driver.quit)
    return driver


@pytest.mark.test5
def test_check_countries(set_driver):
    driver = set_driver
    url = "http://localhost/admin/?app=countries&doc=countries"
    driver.get(url)
    driver.find_element_by_xpath('//input[@name="username"]').send_keys("admin")
    driver.find_element_by_xpath('//input[@name="password"]').send_keys("admin")
    driver.find_element_by_xpath('//button[@name="login"]').click()
    assert driver.find_element_by_xpath(
        '//div[@class="logotype"]').is_displayed()

    countries = driver.find_elements_by_xpath("//table//tr[@class='row']")

    list_countries = []
    zones = []

    for country in countries:
        country_name = country.find_element_by_xpath('./td/a')
        list_countries.append(country_name.text)
        zone = country_name.find_element_by_xpath(
            './parent::*//following-sibling::td[1]')
        if zone.text != "0":
            zones.append(country_name.text)

    assert list_countries == sorted(list_countries)


    for zone in zones:
        link_country = driver.find_element_by_xpath(
            '//td/a[text()="%s"]' % str(zone))
        link_country.click()

        country_name = driver.find_elements_by_xpath(
            '//input[@type="hidden"][contains (@name, "[name]")]')

        states = []
        for country in country_name:
            states.append(country.get_attribute('value'))
        assert states == sorted(states)

        driver.back()


@pytest.mark.test5
def test_check_section_zone(set_driver):
    driver = set_driver
    url = "http://localhost/admin/?app=geo_zones&doc=geo_zones"
    driver.get(url)
    driver.find_element_by_xpath('//input[@name="username"]').send_keys("admin")
    driver.find_element_by_xpath('//input[@name="password"]').send_keys("admin")
    driver.find_element_by_xpath('//button[@name="login"]').click()
    assert driver.find_element_by_xpath('//div[@class="logotype"]').is_enabled()

    countries = driver.find_elements_by_xpath(
        "//table//tr[@class='row']//td[5]/a")

    idx=0
    while idx < len(countries):
        countries = driver.find_elements_by_xpath(
            "//table//tr[@class='row']//td[5]/a")
        countries[idx].click()
        select_zone = driver.find_elements_by_xpath(
            '//select[contains (@name, "zone_code")]//option[@selected="selected"]')
        zone_list = []
        for zone in select_zone:
            zone_list.append(zone.text)
        assert zone_list == sorted(zone_list)
        idx +=1
        driver.back()
