if __name__=='__main__':
    from urllib.request import urlopen
    from urllib.error import HTTPError
    from bs4 import BeautifulSoup
    from selenium import webdriver
    import time
    import re

    # bsObj = BeautifulSoup(urlopen("http://www.toutiao.com").read(), features='html.parser')
    # print(bsObj.html)


    pages = []
    def loopSingleSite(uri):
        print("uri     ==========>"+uri)
        driver = webdriver.Chrome('C:/Users/bill_wang/chromedriver_win32/chromedriver')
        if "http" in uri or "www" in uri:
            whole_uri = uri
        elif uri.startswith("avascript"):
            return
        else:
            whole_uri = "https://www.toutiao.com" + uri
        print("whole_uri==========>"+whole_uri)
        driver.get(whole_uri)
        if whole_uri in pages:
            return
        pages.append(whole_uri)

        driver.implicitly_wait(10)
        bsObj = BeautifulSoup(driver.page_source, features='html.parser')
        for link in bsObj.find_all('a'):
            print(link.get("href"))
            loopSingleSite(link.get("href")[1:])
        driver.close()

    loopSingleSite("/")














