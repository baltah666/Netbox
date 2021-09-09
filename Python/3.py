import requests
import json

url = "http://192.168.174.149:8000/api/dcim/devices"

payload={}
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Token 0123456789abcdef0123456789abcdef01234567'
}

response = requests.request("GET", url, headers=headers, data=payload)
json_data = response.json()
results = json_data['results']

for device in results:
	hostname = device['name']
	ipaddr = device[ 'primary_ip' ][ 'address' ]
	print('The IP address of' + hostname + 'is' + ipaddr)
	
#print(response.text)
