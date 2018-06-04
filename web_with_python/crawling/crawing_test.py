# -*- coding:utf-8 -*-

"""
맛집을 알려주는 다이닝 코드에서
구로 디지털 단지역 근처 맛집의 이름을 긁어옴
"""

import requests
from bs4 import BeautifulSoup

req = requests.get('https://www.diningcode.com/list.php?query=%EA%B5%AC%EB%A1%9C%EB%94%94%EC%A7%80%ED%84%B8%EB%8B%A8%EC%A7%80')
html = req.text

soup = BeautifulSoup(html,'html.parser')

titles = soup.findAll(class_='dc-restaurant-name')

for title in titles:
    print(title.get_text())

for img in imgs:
    print(img)