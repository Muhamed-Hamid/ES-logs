import requests
import json

def search(num):
	url = 'https://search##/_search?q=to:' + str(num)
	encode = url.replace(' ','%20')
	r = requests.get(url)
	j = r.json()
	#parse our required fields only
	for log in j['hits']['hits']:
		Date = print(log['_source']['date'])
		To = print(log['_source']['to'])
		From = print(log['_source']['from'])
		Oid = print(log['_source']['id'])
		SMSC = print(log['_source']['smsc'])
		udh = print(log['_source']['udh'])
