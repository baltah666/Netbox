from netbox import NetBox
netbox = NetBox(host='192.168.174.149',port=80,use_ssl=False, auth_token='0123456789abcdef0123456789abcdef01234567')

nb_dev_role = netbox.dcim.get_device_roles()
print(nb_dev_role)
