#! python3
#  searchpypi - A short Script that Opens several search results from pypi.org
# Usage

# searchpypi.py [keyword]
# Example: searchpypi.py boring stuff


import requests, sys, webbrowser, bs4

print(f'Searching ...')
res = requests.get('https://pypi.org/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

# Retrieving Top Search Resluts Links
soup = bs4.BeautifulSoup(res.text, 'html.parser')
# Open a new Tab for each result
linkElems = soup.select('.package-snippet')


# Opening Web Browser for Each Result
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    urlToOpen = 'https://pypi.org' + linkElems[i].get('href')
    print(f'Opening {urlToOpen}')
    webbrowser.open(urlToOpen)