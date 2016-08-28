#!/usr/bin/python
#coding=utf-8

import requests
import re
import codecs
import os
from bs4 import BeautifulSoup
from jinja2 import Environment, FileSystemLoader

root_url = 'http://1024.05et.net/pw/'

#base_url = 'http://1024.05et.net/pw/thread.php?fid=7&page=%d'
base_url = 'http://1024.05ia.club/pw/thread.php?fid=5&page=%d'

#keywords = ['Naturals', 'Blacked', 'X-Art', 'Wow', 'Babes', 'Anjelica', 'BLACKED', '18OnlyGirls',
#            'SexArt', 'Colette']`
keywords = ['ASIA']

match = '^htm_data'

wanted = []
for i in range(1, 50):
    r = requests.get(base_url % i)

    r.encoding = 'utf-8'
    html = r.text
    
    soup = BeautifulSoup(html, 'html.parser')
    
    for link in soup.find_all(href=re.compile('^htm_data')):
        if not link.string:
            continue
        for word in keywords:
            if word in link.string:
                print link.string
                wanted.append({'link': root_url+link.get('href'), 'text': link.string})

THIS_DIR = os.path.dirname(os.path.abspath(__file__))
env = Environment(loader=FileSystemLoader(THIS_DIR))
template = env.get_template('template/my.template')

content = template.render(wanted=wanted)

fp = codecs.open('./my.html', 'w', 'utf-8')
fp.write(content)
fp.close()
