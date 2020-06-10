import os
from applitools.selenium.eyes import Eyes
#from applitools.images import Eyes
from applitools.core import Region
#from applitools.images import Target
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

uri = "https://www.ibrance.com/"
eyes = Eyes()
eyes.api_key = 'tVfCNAnM3xpan3kF68100LyvKe2egwuiu22AtvboGmHbY110'
#eyes.api_key = api_key
eyes.force_full_page_screenshot = True
driver = webdriver.Chrome(r'D:\github\github-jenkins-integration-test\chromedriver.exe')
driver.maximize_window()


def hover_menu(driver):
    time.sleep(5)
    sub_menu = driver.find_element_by_css_selector(".ibrance-overview-submenu")
    print("line 1")
    hov = ActionChains(driver).move_to_element(sub_menu)
    print("line 2")
    hov.perform()
    time.sleep(5)


try:
    driver = eyes.open(driver=driver, app_name='ibrance', test_name='ibrance homepage')
    driver.get(uri)
    #eyes.check_window('Home Page')
    time.sleep(5)

    #driver.find_element_by_css_selector(".menu > .menu__item.is-expanded:nth-child(2)").click()
    driver.find_element_by_css_selector(".menu__item .about-ibrance-menu")
    time.sleep(5)
    hover_menu(driver)

    '''sub_menu = driver.find_element_by_css_selector(".ibrance-overview-submenu")
    ActionChains(driver).move_to_element(sub_menu).perform()'''


finally:
    eyes.abort_if_not_closed()

