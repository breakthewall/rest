#!/bin/bash

pip install --upgrade pip
pip install requests
echo -e "
import requests
r = requests.post('http://flask:8000/default', 'http://nvie.com')
print(r.content)
" | python3
