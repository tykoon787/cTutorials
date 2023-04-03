print('-------------------------------')
print('Opening a browser to a URL')
print('-------------------------------')

import webbrowser

webbrowser.open('https://www.google.com')

print('-------------------------------')
print('Download Files from the Web with request Module')
print('-------------------------------')

import requests

res = requests.get('https://www.automatetheboringstuff.com/files/rj.txt')
print(type(res))

res.status_code == requests.codes.ok
print(res.status_code)

print(len(res.text))
print(res.text[:250])  # Will Print the first 250 characters of the Page

print('-------------------------------')
print('Handling Download Erros')
print('-------------------------------')

import requests
res = requests.get('https://inventwithpython.com/page_that_does_not_exist')
try:
 res.raise_for_status()  # If an error occurs when downloading the webpage, the program will crash. Else if no errors
 # occur, then it won't do anything
except Exception as exc:
 print(f'There was a problem: {exc} ')

print('-------------------------------')
print('Saving Download Files to the Hard-drive')
print('-------------------------------')

import requests

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
res.raise_for_status()
fileName = 'RomeoAndJuliet.txt'
playFile = open(fileName, 'wb')  # 'wb' means write in binary form so that we can maintain unicode encoding of the text.

for chunk in res.iter_content(100000):
    playFile.write(chunk)

playFile.close()

from pathlib import Path
cwd = Path.cwd()
print(f'File Successfully Downloaded and saved in {cwd}\\{fileName} ')

# The iter_content() method returns “chunks” of the content on each
# iteration through the loop. Each chunk is of the bytes data type, and you
# get to specify how many bytes each chunk will contain. One hundred
# thousand bytes is generally a good size, so pass 100000 as the argument
# to iter_content()

print('-------------------------------')
print('Saving to hardrive using os')
print('-------------------------------')

# Saving the image to ./xkcd
import os
fileName = 'comic'
imgFile = open(os.path.join('xkcd', os.path.basename(fileName)), 'wb')

for chunk in res.iter_content(100000):
    imgFile.write(chunk)

from pathlib import Path

cwd = Path.cwd()
print(f'Image Successfully Saved in {cwd}\\{fileName}')

imgFile.close()

print('-------------------------------')
print('Parsing HTML with Beautiful Soup')
print('-------------------------------')

import bs4, requests

res = requests.get('https://nostarch.com')
res.raise_for_status()
nostarchSoup = bs4.BeautifulSoup(res.text, 'html.parser')
print(type(nostarchSoup))

exampleFile = open('parsableHtml.html')
exampleSoup = bs4.BeautifulSoup(exampleFile, 'html.parser')
print(type(exampleSoup))

print('---------------------------------------')
print('Finding Specific Elements with Select()')
print('---------------------------------------')

newHTMLFile = open('parsableHtml.html')
newHTMLFileSoup = bs4.BeautifulSoup(newHTMLFile.read(), 'html.parser')
elems = newHTMLFileSoup.select('#author')  # We use Select to return a list of all elements with id=author
print(type(elems))
print(len(elems))  # This will let us know how many tag objects are there. In this case it was one (1)
print(type(elems[0]))
print(str(elems[0]))  # The tag object as a string
print(elems[0].getText())  # This will return the element's text
print(elems[0].attrs)

print('---------------------------------------')
print('Pulling <p> elements, As an example')
print('---------------------------------------')

pElems = newHTMLFileSoup.select('p')
print(len(pElems))
print(str(pElems[0]))

for i in range(len(pElems)):
    print(pElems[i].getText())

print('---------------------------------------')
print('Getting Data From an Elements Attribute')
print('---------------------------------------')

# We use the get() method which makes it possible to access attribute values from an element

soup = bs4.BeautifulSoup(open('parsableHtml.html'), 'html.parser')
spanElem = soup.select('span')[0]  # We use select to find any <span> Elements. Then we store the first match to spanElem Variable
print(str(spanElem))
print(spanElem.get('id'))
spanElem.get('some_nonexistent_addrr') == None
print(spanElem.attrs)