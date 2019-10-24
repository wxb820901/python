if __name__ == '__main__':
    from bs4 import BeautifulSoup
    from selenium import webdriver
    import requests
    import urllib3.parse as urlparse


    pages = []
    base_url = "https://www.toutiao.com"


    def loopSingleSite(url):
        if url in pages:
            return
        print(url)
        pages.append(url)

        try:
            driver = webdriver.Chrome('C:/Users/bill_wang/chromedriver_win32/chromedriver')
            driver.implicitly_wait(30)
            if requests.get(url).status_code == 200:
                driver.get(url)
                bsObj = BeautifulSoup(driver.page_source, features='html.parser')
                # printAllLink(bsObj)
                for link in bsObj.find_all('a'):
                    innerUrl = urlparse(link.get("href"))
                    print("uri ==> " + url, " innerUrl ==>" + innerUrl)
                    if innerUrl.geturl().startswith('http'):
                        loopSingleSite(innerUrl.geturl())
                    elif innerUrl.geturl().startswith('//'):
                        loopSingleSite("http:" + innerUrl.geturl())
                    else:
                        return

        # except BaseException as e:
        #     print("error: ", str(e))
        finally:
            driver.close()


    loopSingleSite(base_url)
