#!/usr/bin/env python

import sys
import requests
from bs4 import BeautifulSoup
from dateutil.parser import parse

def unicode_truncate(s, length, encoding='utf-8'):
    encoded = s.encode(encoding)[:length]
    return encoded.decode(encoding, 'ignore')

request = requests.get('http://www.cs.rochester.edu/dept/seminar/rss')
soup = BeautifulSoup(request.text, "lxml")
items = soup.find_all('item')
for item in items:
    title = item.find('title').text
    link = item.find('guid').text
    description = item.find('description').text
    decription = unicode_truncate(description, 75)
    date = item.find('ev:startdate').text
    pdate = parse(date)
    print title + ' - ' + link + ' - ' + pdate.strftime('%d/%m - %H:%M')
#    print description
