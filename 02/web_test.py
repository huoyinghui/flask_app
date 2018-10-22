# -*- coding:utf-8 -*-
import requests


resp = requests.get('http://localhost:8000')
print(resp)
assert resp.status_code == 200
