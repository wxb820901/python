import nmap


def nmapScan(tgtHosts, tgtPorts):
    nmScan = nmap.PortScanner()
    nmScan.scan(tgtHosts, tgtPorts)
    print(tgtHosts + ":" + tgtPorts + "==>" + str(nmScan[tgtHosts]))

nmapScan("10.22.17.24","1-65000")