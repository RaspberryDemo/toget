#!/usr/bin/python
#coding=utf-8

import requests
import re
import codecs
import os
from bs4 import BeautifulSoup
from jinja2 import Environment, FileSystemLoader

'''cb1024 aisa'''
#root_url = 'http://1024.05et.net/pw/'
#base_url = 'http://1024.05ia.club/pw/thread.php?fid=5&page=%d'
#keywords = ['kin8']
#charset = 'utf-8'

'''bt1024 us'''
#root_url = 'http://1024.05et.net/pw/'
#base_url = 'http://1024.05et.net/pw/thread.php?fid=7&page=%d'
#keywords = ['Naturals', 'Blacked', 'X-Art', 'Wow', 'Babes', 'Anjelica', 'BLACKED', '18OnlyGirls',
#            'SexArt', 'Colette']
#charset = 'utf-8'

'''caoliu'''
#root_url = 'http://cl.vtcjd.com/'
#base_url = 'http://cl.vtcjd.com/thread0806.php?fid=2&search=&page=%d'
#keywords = ['kin8']
#charset = 'gb2312'

'''caoliu us'''
root_url = 'http://cl.vtcjd.com/'
base_url = 'http://cl.vtcjd.com/thread0806.php?fid=4&search=&page=%d'
keywords = ['Naturals', 'Blacked', 'X-Art', 'Wow', 'Babes', 'Anjelica', 'BLACKED', '18OnlyGirls',
            'SexArt', 'Colette']
charset = 'gb2312'

match = '^htm_data'

wanted = []
for i in range(1, 50):
    r = requests.get(base_url % i)

    r.encoding = charset
    html = r.text
    
    soup = BeautifulSoup(html, 'html.parser')
    
    for link in soup.find_all(href=re.compile('^htm_data')):
        if not link.string:
            continue
        for word in keywords:
            if word in link.string:
                s = link.string
                print s
                wanted.append({'link': root_url+link.get('href'), 'text': s})

THIS_DIR = os.path.dirname(os.path.abspath(__file__))
env = Environment(loader=FileSystemLoader(THIS_DIR))
template = env.get_template('template/my.template')

content = template.render(charset='utf-8', wanted=wanted)

fp = codecs.open('./my.html', 'w', 'utf-8')
fp.write(content)
fp.close()
