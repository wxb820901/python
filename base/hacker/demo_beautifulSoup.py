#!python3

import bs4
import requests

def getByUrl(url):
    res = requests.get(url)
    res.raise_for_status()
    return res.text

bcontent = bs4.BeautifulSoup(getByUrl('https://www.jetbrains.com/help/pycharm/installing-uninstalling-and-upgrading-packages.html'))
print(str(type(bcontent)))
print('-----------------------------------------------')
print(str(bcontent.select('p')))
print('-----------------------------------------------')
print(str(bcontent.select('p > a')))
print('-----------------------------------------------')
print(str(bcontent.select('p[data-swiftype-index="false"]')))