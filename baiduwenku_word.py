#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from selenium import webdriver
from bs4 import BeautifulSoup
import re
import time

options = webdriver.ChromeOptions()
# options.add_argument('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36')
chrome_driver = 'F:\Chrome_driver\chromedriver.exe'
browser = webdriver.Chrome(executable_path=chrome_driver)
browser.get('https://wenku.baidu.com/view/c47d51e0a45177232f60a2e5.html')
# page = browser.find_elements_by_xpath("//div[@class='page']")
# browser.execute_script('arguments[0].scrollIntoView();', page[-1])  # 拖动到可见的元素去
# nextpage = browser.find_element_by_xpath("//p[@class='down-arrow goBtn']")
# nextpage.click()
# time.sleep(5)
html = browser.page_source
# m = BeautifulSoup(html, 'lxml')
# result = m.find_all('p', class_='reader-word-layer')
# print(result)
reg = r'<p class="reader-word-layer([\s\S]+?)">([\s\S]+?)</p>'  # 正则表达式匹配内容
pattern = re.compile(reg)
tags = re.findall(pattern, html)
art = []
# for te in tags:
#     mid = te.text.scrip()
#     art.append(mid)
# print(art)
for s in tags:
    mid = s[1]
    art.append(mid)
print(art)

