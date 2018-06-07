# -*- coding:utf-8 -*-
"""
1. user-agent로 headless 크롬을 탐지하지하는 것을 막기 위해 user-agent 값을 변경함

2. 크롬에는 플러그인이 설치되어있는데 headless는 플러그인이 하나도 로딩되지 않으므로 0개임
자바 스크립트로 플러그인 개수를 알아내 탐지하는 것을 막기 위해 가짜 플러그인 리스트를 넣어줌

3. 브라우저에는 언어 설정이 되어있지만 headless모드는 언어설정이 되어있지 않음.
탐지를 막기 위해 언어 설정을 넣어줌
"""
from selenium import webdriver

TEST_URL = 'https://intoli.com/blog/making-chrome-headless-undetectable/chrome-headless-test.html'
options = webdriver.ChromeOptions()
options.add_argument('headless') # 크롬이 headless모드(창이 없는)로 동작하게 만들어줌
options.add_argument('window-size=1920x1080')
options.add_argument('disable-qgu')
# 1. headless 탐지를 막기 위해서 user-agent 값 변경
options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")
# 3. 언어 설정
options.add_argument("lang=ko_KR")

driver = webdriver.Chrome('/Users/gong-yong1/Downloads/chromedriver',chrome_options=options)

driver.get(TEST_URL)

# 2. 가짜 플러그인 추가
# js로 nviagator 객체의 plugins 속성 자체를 ㄹ오버라이딩해 임의의 배열을 반환하도록 만듬
driver.execute_script("Object.defineProperty(navigator, 'plugins', {get: function() {return[1, 2, 3, 4, 5];},});")
driver.execute_script("Object.defineProperty(navigator, 'languages', {get: function() {return ['ko-KR', 'ko']}})")



user_agent = driver.find_element_by_css_selector('#user-agent').text
plugins_length = driver.find_element_by_css_selector('#plugins-length').text
languages = driver.find_element_by_css_selector('#languages').text

print('User-Agent:',user_agent)
print('Plugin length:',plugins_length)
print('Languages:',languages)

driver.quit()
