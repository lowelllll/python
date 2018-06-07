# -*- coding : utf-8 -*-
"""
selenium으로 크롤러 만들기
"""

from selenium import webdriver
from bs4 import BeautifulSoup as bs

# Chrome
driver = webdriver.Chrome('/Users/gong-yong1/Downloads/chromedriver')

# PhantomJS
# driver = webdrivre.PhantomJS('/Users/gong-yong1/Downloads/phantomjs')

driver.implicitly_wait(3) # Selenium은 기본적으로 웹 자원들이 모두 로드 될 때 까지 기다리지만
# 암묵적으로 모든 자원이 로드될때 까지 기다리게 하는 시간을 지정함. 3초

driver.get("https://nid.naver.com/nidlogin.login") # url에 접근

# 아이디 비밀번호 입력
driver.find_element_by_name('id').send_keys('id')
driver.find_element_by_name('pw').send_keys('pw')

# 로그인 버튼 누름
driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()

# Naver 페이 들어가기 (주문 내역 확인)
driver.get('https://order.pay.naver.com/home')
html = driver.page_source # 현재 렌더링 된 페이지의 elements를 모두 가져옴 (req.text)
soup = bs(html,'html.parser')
notices = soup.select('div.p_inr > div.p_info > a > span')

for n in notices:
    print(n.text.strip()) # 주문 내역 크롤링


