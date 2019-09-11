import requests
import re
from scapy.all import *

while(True):
    try:
        x = requests.get('your website')
        a=re.findall("regex to get the ip from website",x.text)
        p=IP(dst=a[0],id=1111,ttl=99)/TCP(sport=RandShort(),dport=[22,80],seq=12345,ack=1000,window=1000,flags="S")
        ls(p)
        ans,unans=srloop(p,inter=0.3,retry=2,timeout=4)
        ans.summary()
        unans.summary()
        ans.make_table(lambda s,r: s.dst, s.dport, r.sprintf("%IP.id% \t %IP.ttl% \t %TCP.flags%"))
    except:
        pass
    


