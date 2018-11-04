import pytest

from selenium import webdriver


@pytest.fixture()
def set_driver(request):
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    request.addfinalizer(driver.quit)
    return driver

@pytest.mark.test3
def test_login(set_driver):
    driver = set_driver
    url = "http://localhost/admin/"
    driver.get(url)
    driver.find_element_by_xpath('//input[@name="username"]').send_keys("admin")
    driver.find_element_by_xpath('//input[@name="password"]').send_keys("admin")
    driver.find_element_by_xpath('//button[@name="login"]').click()
    assert driver.find_element_by_xpath('//div[@class="logotype"]').is_enabled()

    menu = driver.find_elements_by_id("app-")

    idx=0
    while idx < len(menu):
        menu = driver.find_elements_by_xpath("//li[@id='app-']")
        section=menu[idx]
        section.click()
        h1 = driver.find_element_by_xpath('//h1').text
        extra_sections = driver.find_elements_by_xpath("//ul[@class='docs']/li")
        if extra_sections:
            extra_idx=0
            while extra_idx < len(extra_sections):
                extra_sections = driver.find_elements_by_xpath("//ul[@class='docs']/li")
                extra = extra_sections[extra_idx]
                extra.click()
                h1 = driver.find_element_by_xpath('//h1').text
                assert len(h1) > 0
                extra_idx +=1
        else:
            assert len(h1) > 0
        idx+=1
