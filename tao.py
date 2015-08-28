#!/usr/bin/env python

from bs4 import BeautifulSoup
import urllib2
from random import randint
def main():
	if internet() == True:
		# Open HTML file
		url = "http://www.mit.edu/~xela/tao.html"
		page = urllib2.urlopen(url)
		doc = BeautifulSoup(page.read(), "lxml")

		# Prepare array to store data
		entries = []

		# Find all 'h4' tags
		for section in doc.find_all('h4'):

		  # Get header text
		  header = section.find_all(text=True)[0]

		  # Get paragraph content
		  # ... don't forget about Unicode
		  content = u""

		  # Find next tag
		  for p in section.find_next_siblings():

		    # ... if it's 'h4' tag - then stop, as we reached next proverb
		    if p.name == 'h4':
		      break

		    # Take care of newline characters
		    # ... and tell Python to treat it as Unicode
		    content += unicode(p.getText())

		# Add new header plus its content into array
		  entries.append({ 'header': header, 'content': content})

		# Chose randomly from set of proverbs
		rand = randint(0,len(entries)-1)

		print '\033[1m'
		print(entries[rand].get('header'))
		print '\033[0m'
		print(entries[rand].get('content'))
		return 0
	return 1

def internet():
    try:
        response = urllib2.urlopen('http://google.com', timeout=1)
	return True
    except urllib2.URLError as err: pass
    return False

main()
