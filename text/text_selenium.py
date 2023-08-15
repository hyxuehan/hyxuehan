from selenium import webdriver
from selenium.webdriver.common.by import By
import time

option = webdriver.EdgeOptions()
option.add_experimental_option('detach',True)
driver = webdriver.Edge(options=option)
driver.get('http://fanyi.baidu.com/')
# while True:
#     a = input('>>')
desktop_guide_close = driver.find_element(
    By.CLASS_NAME, value='desktop-guide-close')
desktop_guide_close.click()

baidu_translate_input = driver.find_element(value='baidu_translate_input')
baidu_translate_input.send_keys('你好')
translate_button = driver.find_element(value='translate-button')
translate_button.click()
time.sleep(2)
try:
    result = driver.find_element(By.XPATH,
                                 value='/html/body/div[1]/div[2]/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div[1]/p[2]')
    print(result.text)
except Exception as ex:
    print(ex)

while True:
    a = input('>>')