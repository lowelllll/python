# -*- coding:UTF-8 -*-
"""
크롤링한 데이터를 python파일과 같은 위치에 result.json을 만들어 저장함
naver 웹툰 title 긁어옴
"""
import requests
from bs4 import BeautifulSoup
import json
import os

# 현재 python 파일의 위치
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

req = requests.get("http://comic.naver.com/webtoon/weekday.nhn")

html = req.text
soup = BeautifulSoup(html,'html.parser')

webtoon_titles = soup.findAll('a',{'class':'title'})

data = {}

for title in webtoon_titles:
    print(title.get_text())
    data[title.get_text()] = title.get('href') # href 속성을 얻음

with open (os.path.join(BASE_DIR,'result.json'),'w+') as json_file:
    json.dump(data,json_file,ensure_ascii=False)

    # json.dumps 일반 스트링
    # json.dump socket,file 에서 사용

