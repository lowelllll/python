# -*- coding:utf-8 -*-
"""
블로그의 제목과 링크를 크롤링
"""
import requests
from bs4 import BeautifulSoup as bs
import os
from django.core.wsgi import get_wsgi_application

# python이 실행될 때 django_settings_module 이라는 한경 변수에 현재 프로젝트의 settings.py 경로를
# 등록

os.environ['DJANGO_SETTINGS_MODULE'] = 'webserver.settings'
application = get_wsgi_application()

# django를 가져와 장고 프로젝트를 사용할 수 있도록 환경을 만듬

import django
django.setup()

# 이 파일을 단독적으로 실행하더라도 마치 manage.py 를 통해 django를 구동한 것 같이
# 장고 환경을 사용할 수 있음


from parsed_data.models import BlogData

def parse_blog():
    req = requests.get('https://beomi.github.io/beomi.github.io_old/')
    html = req.text
    soup = bs(html,'html.parser')
    my_titles = soup.select(
        'h3 > a'
    )
    data = {}

    for title in my_titles:
        data[title.text] = title.get('href')
    return data


# 직접 파일을 실행했을 때
if __name__ == '__main__':
    blog_data_dict = parse_blog()
    print(blog_data_dict)
    for t,l in blog_data_dict.items():
        BlogData(title=t,link=l).save()