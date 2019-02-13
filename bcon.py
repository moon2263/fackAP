from multiprocessing import Pool
from scapy.all import *

def mySendp(x):
	ssidList = ['Frozen','Let_it_go','do_you_wanna_be_a_snow_man?','love_is_open_door','LionKing','scar','simba']
	rMac = "ff:ff:ff:ff:ff:ff"
	sMac = RandMAC()
	dot11 = Dot11(type=0,subtype=0x08,addr1=rMac,addr2=sMac,addr3=sMac)
	bcon = Dot11Beacon()
	essid = Dot11Elt(ID='SSID',info=ssidList[x],len=len(ssidList[x]))
	frame = RadioTap()/dot11/bcon/essid
	sendp(frame,iface='mon0',inter=0.100,loop=1)

pool = Pool(7)
pool.map(mySendp,range(7))

