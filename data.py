import psutil
from time import *
from matplotlib.pyplot import *
from matplotlib import rcParams
from random import *
from easygui import *

data=psutil.net_io_counters(pernic=True)
print(data)
'''
{'本地连接* 1': snetio(bytes_sent=0, bytes_recv=0, packets_sent=0, packets_recv=0, errin=0, errout=0, dropin=0, dropout=0),
 '本地连接* 2': snetio(bytes_sent=0, bytes_recv=0, packets_sent=0, packets_recv=0, errin=0, errout=0, dropin=0, dropout=0), 
 'WLAN': snetio(bytes_sent=0, bytes_recv=0, packets_sent=0, packets_recv=0, errin=0, errout=0, dropin=0, dropout=0), 
 '以太网': snetio(bytes_sent=556379069, bytes_recv=5429734434, packets_sent=3942478, packets_recv=4845500, errin=0, errout=0, dropin=0, dropout=0), 
 '以太网 3': snetio(bytes_sent=0, bytes_recv=0, packets_sent=0, packets_recv=0, errin=0, errout=0, dropin=0, dropout=0), 
 'SRun3K专用宽带拨号连接': snetio(bytes_sent=468451309, bytes_recv=5364303675, packets_sent=3920930, packets_recv=4702925, errin=0, errout=0, dropin=0, dropout=21), '以太网 2': snetio(bytes_sent=0, bytes_recv=0, packets_sent=0, packets_recv=0, errin=0, errout=0, dropin=0, dropout=0), 'Loopback Pseudo-Interface 1': snetio(bytes_sent=0, bytes_recv=0, packets_sent=0, packets_recv=0, errin=0, errout=0, dropin=0, dropout=0)}

'''
'''
{'以太网': snicstats(isup=True, duplex=<NicDuplex.NIC_DUPLEX_FULL: 2>, speed=100, mtu=1500, flags=''), 
'以太网 2': snicstats(isup=False, duplex=<NicDuplex.NIC_DUPLEX_FULL: 2>, speed=10, mtu=1400, flags=''), 
'以太网 3': snicstats(isup=False, duplex=<NicDuplex.NIC_DUPLEX_FULL: 2>, speed=100, mtu=1500, flags=''), 
'SRun3K专用宽带拨号连接': snicstats(isup=True, duplex=<NicDuplex.NIC_DUPLEX_FULL: 2>, speed=100, mtu=1480, flags=''),
'Loopback Pseudo-Interface 1': snicstats(isup=True, duplex=<NicDuplex.NIC_DUPLEX_FULL: 2>, speed=1073, mtu=1500, flags=''),
'WLAN': snicstats(isup=False, duplex=<NicDuplex.NIC_DUPLEX_FULL: 2>, speed=0, mtu=1500, flags=''), 
'本地连接* 1': snicstats(isup=False, duplex=<NicDuplex.NIC_DUPLEX_FULL: 2>, speed=0, mtu=1500, flags=''),
'本地连接* 2': snicstats(isup=False, duplex=<NicDuplex.NIC_DUPLEX_FULL: 2>, speed=0, mtu=1500, flags='')}

'''

'''
{'以太网': snicstats(isup=True, duplex=<NicDuplex.NIC_DUPLEX_FULL: 2>, speed=100, mtu=1500, flags=''), 
'以太网 2': snicstats(isup=False, duplex=<NicDuplex.NIC_DUPLEX_FULL: 2>, speed=10, mtu=1400, flags=''), 
'以太网 3': snicstats(isup=False, duplex=<NicDuplex.NIC_DUPLEX_FULL: 2>, speed=100, mtu=1500, flags=''), 
'SRun3K专用宽带拨号连接': snicstats(isup=True, duplex=<NicDuplex.NIC_DUPLEX_FULL: 2>, speed=100, mtu=1480, flags=''), 
'Loopback Pseudo-Interface 1': snicstats(isup=True, duplex=<NicDuplex.NIC_DUPLEX_FULL: 2>, speed=1073, mtu=1500, flags=''), 
'WLAN': snicstats(isup=True, duplex=<NicDuplex.NIC_DUPLEX_FULL: 2>, speed=1201, mtu=1500, flags=''), 
'本地连接* 1': snicstats(isup=False, duplex=<NicDuplex.NIC_DUPLEX_FULL: 2>, speed=0, mtu=1500, flags=''), 
'本地连接* 2': snicstats(isup=False, duplex=<NicDuplex.NIC_DUPLEX_FULL: 2>, speed=0, mtu=1500, flags='')}

'''
