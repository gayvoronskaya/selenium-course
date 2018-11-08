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
    assert driver.find_element_by_xpath('//div[@class="logotype"]').is_displayed()

    countries = driver.find_elements_by_xpath("//table//tr[@class='row']")

    list_countries = []
    time_zones = []

    for country in countries:
        country_name = country.find_element_by_xpath('./td[5]/a')
        list_countries.append(country_name.text)
        timezone = country.find_element_by_xpath('./td[6]')
        if timezone.text != "0":
            time_zones.append(country_name.text)

    sorted_list_countries = sorted(list_countries)
    assert list_countries == sorted_list_countries


    for zone in time_zones:
        link_country = driver.find_element_by_xpath('//td/a[text()="%s"]' % str(zone))
        link_country.click()
        country_name = driver.find_elements_by_xpath(
            '//input[contains (@name, "[name]")]')
        for country in country_name:
            sub_countries = []
            sub_countries.append(country.get_attribute('value'))
            sorted_sub_countries = sorted(sub_countries)
            assert sub_countries == sorted_sub_countries
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
        sorted_zone_list = sorted(zone_list)
        assert sorted_zone_list == zone_list
        driver.back()
        idx +=1
