import optparse
from socket import *
from threading import Thread, Semaphore

screenLock = Semaphore(value=1)
def connScan(tgtHost, tgtPort):
    try:
        connSkt = socket(AF_INET, SOCK_STREAM)
        connSkt.connect((tgtHost, tgtPort))
        connSkt.send("violentPy\r\n")
        results = connSkt.recv(100)
        screenLock.acquire()
        print("[+]%d/tcp open ", tgtPort)
        print("[+]"+str(results))
        connSkt.close()
    except:
        # print("[-]%d/tcp closed ", tgtPort)
        return

def portScan(tgtHost, tgtPorts):
    try:
        tgtIp = gethostbyname(tgtHost)
    except:
        print("[-]cannot resolve '%s':Unknown host", tgtHost)
        return

    try:
        tgtName = gethostbyaddr(tgtIp)
        print("\n[+] scan results for : " + tgtName[0])
    except:
        print("\n[-] scan results for : " + tgtIp)

    # setdefaulttimeout(1)

    for tgtPort in tgtPorts:
        # print("Scanning port" + str(tgtPort))
        # connScan(tgtHost, tgtPort)
        t = Thread(target=connScan, args=(tgtHost, tgtPort))
        t.start()

#
# ports = list(range(1, 65000))
# print("scan ip 127.0.0.1 ports " + str(ports))
# portScan("localhost", ports)

#==================================
