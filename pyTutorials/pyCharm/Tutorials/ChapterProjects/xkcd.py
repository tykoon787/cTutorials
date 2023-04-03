#! python3

# xkcd Comic Downloader

import requests, bs4, os, sys

url = 'https://www.xkcd.com'
os.makedirs('xkcd', exist_ok=True)

while not url.endswith('#'):
    print(f'Downloading Page {url} ...')
    res = requests.get(url)
    res.raise_for_status()

    # Finding URL of the comic image
    parsedComicHTML = bs4.BeautifulSoup(res.text, 'html.parser')  # Storing the parsed html to a var
    imgElem = parsedComicHTML.select('#comic img')  # Selecting Image where id=comic
    print(imgElem)
    print(imgElem[0].get('src'))
    # Downloading the Image
    if imgElem == []:
        print('Could Not Find an Image')
    else:
        imgUrl = 'https:' + str(imgElem[0].get('src'))
        print(f'Downloading Image {imgUrl} ... ')
        res = requests.get(imgUrl)
        res.raise_for_status()

    # Saving the image to ./xkcd
    imgFile = open(os.path.join('xkcd', os.path.basename(imgUrl)), 'wb')

    for chunk in res.iter_content(100000):
        imgFile.write(chunk)

    from pathlib import Path
    cwd = Path.cwd()
    print(f'Image Successfully Saved in {cwd}\\{imgUrl}')

    imgFile.close()

    # Getting the Prev Button URL
    prevBtnUrl = parsedComicHTML.select('a[rel="prev"]')[0]
    url = 'https://xkcd.com' + prevBtnUrl.get('href')

print('All Comics Downloaded')