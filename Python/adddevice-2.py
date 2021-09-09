import pynetbox
import time

def adddev(dev):
    nb = pynetbox.api(url='http://192.168.174.149:8000/',token='0123456789abcdef0123456789abcdef01234567')
				   
    result = nb.dcim.devices.create(
	name=dev,
	device_type=5,
	device_role=2,
	site=3,
	)
	print(result)
		 
file1 = open ('/home/gns3/Netbox/Python/hosts.txt', 'r')
Lines = file1.readlines()
count = 0
for line in lines:
    count += 1
    time.sleep(0.5)
    dev = line
    adddev(dev)
