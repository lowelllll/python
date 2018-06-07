# -*- coding:utf-8 -*-
"""
새 글이 올라오면 텔레그램 봇을 통해 알려주는 프로그램
자동으로는 안댐.
"""
import requests
from bs4 import BeautifulSoup as bs
import os

import telegram

bot = telegram.Bot(token='604056453:AAEw6z0jSZdYBgzLCbK2kNqCbseiHw-gK-U')

chat_id = bot.getUpdates()[-1].message.chat.id

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

req = requests.get('https://www.clien.net/service/board/sold')
html = req.text
soup = bs(html,'html.parser')

posts = soup.findAll('span',{'data-role':'list-title-text'})

latest = posts[0].text

with open(os.path.join(BASE_DIR,'latest.txt'),'r+') as f_read:
    before = f_read.readline()
    if before != latest:
        bot.sendMessage(chat_id=chat_id,text='새글이 올라왔어요!')
    else:
        bot.sendMessage(chat_id=chat_id,text='새글이 없어요 ㅜㅜ')
    f_read.close()

# latest 파일에 가장 최신 글의 제목이 저장됨
with open(os.path.join(BASE_DIR,'latest.txt'),'w+') as f_write:
    f_write.write(latest)
    f_write.close()


