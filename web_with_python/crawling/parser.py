# -*- coding:utf-8 -*-
"""
session을 이용해 로그인하기
"""
import requests
from bs4 import BeautifulSoup as bs

# 로그인할 유저 정보
LOGIN_INFO = {
    'userID':'lowell2735',
    'userPassword':'asdzxc2978'
}

with requests.session() as s:
    first_page = s.get('https://www.clien.net/service')
    html = first_page.text
    soup = bs(html,'html.parser')
    csrf = soup.find('input',{'name':'_csrf'}) # input 태그 중 name이 _csrf인 것을 찾음
    print(csrf['value'])

    # python3에서 두 dict을 합치는 방법 {**dict1,**dict2}으로 dict들을 unpacking 하는 것
    LOGIN_INFO = {**LOGIN_INFO,**{'_csrf':csrf['value']}}
    print(LOGIN_INFO)

    # login
    login_req = s.post('https://www.clien.net/service/login',data=LOGIN_INFO)
    print(login_req.status_code)

    # login fail
    if login_req.status_code != 200:
        raise Exception('로그인이 되지 않았어요 아이디와 비밀번호를 다시 확인해 주세요')

    # login success
    # 로그인 세션 유지

    post_one = s.get('https://www.clien.net/service/board/rule/10707408')
    soup = bs(post_one.text,'html.parser')

    # 공지 글과 제목을 집음
    title = soup.select('#div_content > div.post_title.symph_row > h3 > span')
    content = soup.select('#div_content > div.post_view > div.post_content > article > div')
    print(title[0].text) # 글 제목의 문자를 가져옴
    # select로 하나만 가져와도 title 자체는 리스트임
    print(content[0].text)



