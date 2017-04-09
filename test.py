import json
import requests

data = {
	'ID':8,
	'x':563,
	'y':325,
	'rgb':'#FFF'
}

r = requests.post("http://dangaolicksballz-dev.us-west-2.elasticbeanstalk.com/api/update_pixel", json=data)
	
#r = requests.post("http://127.0.0.1:5000/api/update_pixel", json=data)
print(r.json())