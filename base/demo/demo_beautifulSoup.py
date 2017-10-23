#!python3

import bs4
import demo_requests

bcontent = bs4.BeautifulSoup(demo_requests.getByUrl('https://www.jetbrains.com/help/pycharm/installing-uninstalling-and-upgrading-packages.html'))
print(str(type(bcontent)))
print('-----------------------------------------------')
print(str(bcontent.select('p')))
print('-----------------------------------------------')
print(str(bcontent.select('p > a')))
print('-----------------------------------------------')
print(str(bcontent.select('p[data-swiftype-index="false"]')))