import httplib
import requests


payload = {'token': '02cc42245803e6fb65c492a42cd0fa0f'}
url_rev = 'http://challenge.code2040.org/api/reverse'
url_validate = 'http://challenge.code2040.org/api/reverse/validate'

r = requests.post(url_rev, json = payload)

print(r.status_code)
print(r.content)

rev_str = r.content[::-1]
print(rev_str)

payload2 = {'token': '02cc42245803e6fb65c492a42cd0fa0f', 'string' : rev_str}
s = requests.post(url_validate, json = payload2)

print(s.status_code)