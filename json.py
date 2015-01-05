import requests
import json
import datetime as dt
from dateutil import parser

# Registration

url = 'http://challenge.code2040.org/api/register/post'
data = {'email': 'bokoro@caltech.edu', 'github': 'https://github.com/brokoro/code2040'}
headers = {'Content-Type': 'application/json'}
r = requests.post(url, data=json.dumps(data), headers=headers)
identifier = r.json().get('result') 

# Reverse a string

url = "http://challenge.code2040.org/api/getstring/post"
data = {'token': identifier}
r = requests.post(url, data=json.dumps(data), headers=headers)
string = r.json().get('result')

reverse = string[::-1]

url = 'http://challenge.code2040.org/api/validatestring'  
data = {'token': identifier,'string': reverse}
r = requests.post(url, data=json.dumps(data), headers=headers)

# Needlse in haystack

url = 'http://challenge.code2040.org/api/haystack/post'
data = {'token': identifier}
r = requests.post(url, data=json.dumps(data), headers=headers)
dic = r.json().get('result')
needle = dic['needle']
haystack = dic['haystack']
idx = haystack.index(needle) if needle in haystack else None

url = 'http://challenge.code2040.org/api/validateneedle'
data = {'token': identifier,'needle': idx}
r = requests.post(url, data=json.dumps(data), headers=headers)

# Prefix

url = 'http://challenge.code2040.org/api/prefix'
data = {'token': identifier}
r = requests.post(url, data=json.dumps(data), headers=headers)
dic = r.json().get('result')
prefix = dic['prefix']
array = dic['array']
filtered = filter(lambda x: not x.startswith(prefix), array)

url = 'http://challenge.code2040.org/api/validateprefix'
data = {'token': identifier,'array': filtered}
r = requests.post(url, data=json.dumps(data), headers=headers)

# Dating game

url = 'http://challenge.code2040.org/api/time'
data = {'token': identifier}
r = requests.post(url, data=json.dumps(data), headers=headers)
dic = r.json().get('result')
datestamp = dic['datestamp']
interval = dic['interval']
ds = parser.parse(datestamp)
delta = dt.timedelta(seconds = interval)
iso = str(ds + delta) 

url = 'http://challenge.code2040.org/api/validatetime'
data = {'token': identifier,'datestamp': iso}
r = requests.post(url, data=json.dumps(data), headers=headers)

# Grading 

url = 'http://challenge.code2040.org/api/status'
data = {'token': identifier}
r = requests.post(url, data=json.dumps(data), headers=headers)

