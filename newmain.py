from selenium import webdriver
from time import sleep
import datetime
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

file = open('log.txt', 'w')
#driver = webdriver.Chrome()
option = webdriver.ChromeOptions()
option.add_experimental_option('detach', True)
#option.add_argument('--headless')
driver = webdriver.Chrome(options=option)

driver.get('https://www.lambdatest.com/selenium-playground/jquery-dropdown-search-demo')
driver.maximize_window()

sleep(1)

click_drop = driver.find_element(By.XPATH, '//*[@id="__next"]/div/section[2]/div/div/div/div[1]/div[2]/span/span[1]/span')
click_drop.click()
sleep(2)
click_form = driver.find_element(By.XPATH, '/html/body/span/span/span[1]/input')
click_form.send_keys('Japan')
click_form.click()
click_form.send_keys(Keys.ENTER)
file.close()