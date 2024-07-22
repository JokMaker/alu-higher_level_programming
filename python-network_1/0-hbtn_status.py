#!/usr/bin/python3
import urllib.request

url = 'https://alu-intranet.hbtn.io/status'
headers = {'User-Agent': 'Mozilla/5.0'}

request = urllib.request.Request(url, headers=headers)

with urllib.request.urlopen(request) as response:
    body = response.read()

print("Body response:")
print("\t- type: {}".format(type(body)))
print("\t- content: {}".format(body))
print("\t- utf8 content: {}".format(body.decode('utf-8')))
