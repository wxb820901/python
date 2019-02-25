import datetime
import threading
import time

print("time.time() ==> "+ str(time.time()))
time.sleep(1)
print("after 1 seconds "+str(time.time()))
print(datetime.datetime.now())
print(str(datetime.datetime.now().year))
print(str(datetime.datetime.now().month))
print(str(datetime.datetime.now().day))
print(str(datetime.datetime.now().hour))
print(str(datetime.datetime.now().minute))
print(str(datetime.datetime.now().second))
print(str(datetime.datetime.now().second))
dt = datetime.datetime(2017, 1, 2, 3, 4, 5, 100)
print("datetime.datetime(2017, 1, 2, 3, 4, 5, 100 ) ==> "+str(dt))
dt = datetime.datetime.fromtimestamp(1000000)
print("datetime.datetime.fromtimestamp(1000000)     ==> "+str(dt))
dt = datetime.datetime.fromtimestamp(time.time())
print("datetime.datetime.fromtimestamp(time.time()) ==> "+str(dt))
print("datetime.datetime.fromtimestamp(1000000) > datetime.datetime.fromtimestamp(time.time()) ==> " +str(datetime.datetime.fromtimestamp(1000000) > datetime.datetime.fromtimestamp(time.time()) ))

print(datetime.timedelta(1, 1, 1, 1).days)
print(datetime.timedelta(1, 1, 1, 1).seconds)
print(datetime.timedelta(1, 1, 1, 1).total_seconds())#24*60*60+60*60
print(datetime.timedelta(1, 0, 0, 0).total_seconds())#24*60*60


def task1():
    time.sleep(3)
    print("tesk1 over")

threadObj = threading.Thread(target=task1)
threadObj.start()

print("all over before tesk1 over")




