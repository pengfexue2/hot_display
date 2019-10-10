#!/usr/bin/env python
# encoding: utf-8
# @Time : 2019-10-10 20:08

__author__ = 'Ted'

import requests
from bs4 import BeautifulSoup

url = "https://s.weibo.com/top/summary"
headers = {"User-Agent": "", "Cookie": ""}
wb_response = requests.get(url, headers=headers)
webcontent = wb_response.text
soup = BeautifulSoup(webcontent, "html.parser")
index_list = soup.find_all("td", class_="td-01")
title_list = soup.find_all("td", class_="td-02")
level_list = soup.find_all("td", class_="td-03")

topic_list = []
for i in range(len(index_list)):
    item_index = index_list[i].get_text(strip=True)
    if item_index == "":
        item_index = "0"
    item_title = title_list[i].a.get_text(strip=True)
    if title_list[i].span:
        item_mark = title_list[i].span.get_text(strip=True)

    else:
        item_mark = "置顶"
    item_level = level_list[i].get_text(strip=True)
    topic_list.append({"index": item_index, "title": item_title, "mark": item_mark, "level": item_level,
                       "link": f"https://s.weibo.com/weibo?q=%23{item_title}%23&Refer=top"})
print(topic_list)