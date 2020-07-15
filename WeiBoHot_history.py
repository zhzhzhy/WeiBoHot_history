#!/usr/bin/env python3
# -*- coding=UTF-8 -*-

import os
import time
import requests
from lxml import etree

# count chinese characters number
'''
def str_count(str):
    zh_count = 0
    for s in str:
        if '\u4e00' <= s <= '\u9fff':
            zh_count += 1
    return zh_count
'''

url = "https://s.weibo.com/top/summary?cate=realtimehot"
headers={
    'Host': 's.weibo.com',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Referer': 'https://weibo.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'
}

r = requests.get(url,headers=headers)
html_xpath = etree.HTML(r.text)
data = html_xpath.xpath('//*[@id="pl_top_realtimehot"]/table/tbody/tr/td[2]')
num = -1

# Define the store path of files
file_name = time.strftime('%Y{y}%m{m}%d{d}%H{minute}%M',time.localtime()).format(y='-', m='-', d=' ',minute=':')
data_time = time.strftime('%Y{y}%m{m}%d{d}%H{h}',time.localtime()).format(y='年', m='月', d='日',h='时')
year_path = time.strftime('%Y',time.localtime())
month_path = time.strftime('%m',time.localtime())
day_month = time.strftime('%d',time.localtime())
all_path = "./" + year_path + '/'+ month_path + '/' + day_month
if not os.path.exists(all_path):
    # If not exist,create it
    os.makedirs(all_path)

# The destination of files
path = all_path + '/' + file_name +'.md'

# Header of the file
with open(path,'a') as f:
    f.write('{}\n'.format(data_time+'数据'))
    f.write('{}{}{}'.format("Status: ",r.status_code,"\n\n"))
f.close()

for tr in (data):
    title = tr.xpath('./a/text()')
    hot_score = tr.xpath('./span/text()')
#   length = len(str(num)+title[0])+1       #Total length of row char number
#   zh_count = str_count(title[0])          #Number of chinese char(width of two English words)
#   indent = 40-(length-zh_count)-2*zh_count   #Indent of blank space
    num += 1
    # Filter the 0 result
    if num == 0:
        pass
    else:
#        if indent <= 0:
#            indent = 1
        with open(path,'a') as f:
            f.write('{}.{}\n'.format(num,title[0]))
            f.write('{}\n\n'.format('微博热度:'+hot_score[0]))
        f.close()
