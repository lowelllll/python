# -*- coding:utf-8 -*-
"""
창이 없는 크롬을 돌려 스크린샷을 찍는 프로그램
"""
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('headless') # 크롬이 headless모드(창이 없는)로 동작하게 만들어줌
options.add_argument('window-size=1920x1080')
options.add_argument('disable-qgu')
# options.add_argument('--disable-gpu')


driver = webdriver.Chrome('/Users/gong-yong1/Downloads/chromedriver',chrome_options=options)

driver.get('http://google.com')
driver.implicitly_wait(3)
driver.get_screenshot_as_file('google_main.png') # 화면 스크린샷

driver.quit()
