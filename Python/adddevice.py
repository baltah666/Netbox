import pynetbox

dev = "SW10"
def adddev(dev):
    nb = pynetbox.api(url='http://192.168.174.149:8000/', token='0123456789abcdef0123456789abcdef01234567')
				   
    result = nb.dcim.devices.create(
	     name=dev,
	     device_type=5,
             device_role=2,
	     site=3,
    )
    print(result)

adddev(dev)
