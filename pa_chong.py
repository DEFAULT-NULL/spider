#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup

# link = 'https://www.hao123.com'
# m = requests.get(link)
# soup = BeautifulSoup(m.text, 'lxml')
# lii = []
# h = soup.find_all('li', class_='g-gc')
# for each in h:
#     t = each.a.text
#     lii.append(t)
# print(lii)

list_name = []
list_price = []
list_num = []
list_big = []
list_year = []
list_people = []
list_loc = []
list_index = []
for i in range(10):
    link = 'https://beijing.anjuke.com/sales/p'+str(i+1)+'/#'
    m = requests.get(link)
    soup = BeautifulSoup(m.text, 'lxml')
    h = soup.find_all('li', class_='list-item')
    for each in h:
        name = each.find('div', class_='house-title').a.text.strip()
        price = each.find('span', class_='price-det').text.strip()
        num = each.find('div', class_='details-item').span.text.strip()
        big = each.find('div', class_='details-item').contents[3].text.strip()
        year = each.find('div', class_='details-item').contents[7].text.strip()
        people = each.find('div', class_='details-item').contents[8].text.strip()
        loc = each.find('span', class_='comm-address').text.strip()
        index = each.find_all('span', class_='item-tags tag-others')
        tags = [i.text for i in index]
        print(name, price, num, big, year, people, loc, tags)



