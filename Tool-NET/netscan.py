import networkscan

#import scapy.all as scapy
#import argparse
from netbox import NetBox
netbox = NetBox(host='192.168.174.149',port=8000,use_ssl=False, auth_token='0123456789abcdef0123456789abcdef01234567')

if _name_ =='_main_':
    my_network = "192.168.0.0/24"

    my_scan = networkscan.Networkscan(my_network)

    my_scan_run()

    for address in my_scan.list_of_hosts_found:
        print(address)
