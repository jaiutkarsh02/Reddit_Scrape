# -*- coding: utf-8 -*-
"""
Created on Sat May 19 13:55:40 2018

@author: JAI
"""

from bs4 import BeautifulSoup
import json
import requests
from pprint import pprint
from newspaper import Article

with open('redditscraped.json') as f:
    data = json.load(f)
url_data= data["url"]
final=list(url_data.values())

for i in final:
    response = requests.get(i)
    soup = BeautifulSoup(response.content, "html.parser")
    for link in soup.find_all('a'):
        check=link.get('href')
        for j in check:
            article = Article(j)
            article.download()
            article.parse()
            org=article.text

org.to_json("orgtext.json")