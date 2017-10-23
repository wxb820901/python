#!python3

import webbrowser, requests,os
if not os.path.exists(os.getcwd()+os.path.sep+'requestsFolder'):
    os.makedirs(os.getcwd() + os.path.sep + 'requestsFolder')   #mkdir
    # os.rmdir(os.getcwd()+os.path.sep+'ostestfolder')         #rmdir


# webbrowser.open("http://google.com")  #just opne os browser
res = requests.get('https://www.jetbrains.com/help/pycharm/installing-uninstalling-and-upgrading-packages.html')

print(str(type(res)))
print(str(res.status_code))
print(str(len(res.text)))
print(res.text[:250])

res.raise_for_status()
content = open(os.getcwd() + os.path.sep + 'requestsFolder'  + os.path.sep + 'page.html','w')

for chunk in res.iter_content(100000):
    content.write(chunk)

content.close()

def getByUrl(url):
    res = requests.get(url)
    res.raise_for_status()
    return res.text