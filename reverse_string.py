import httplib
import requests


payload = {'token': '02cc42245803e6fb65c492a42cd0fa0f'}
url_rev = 'http://challenge.code2040.org/api/reverse'

r = requests.post(url_rev, json = payload)

print(r.status_code)
print(r.content)
