#!/bin/bash

pip install --upgrade pip
pip install requests
echo -e "import requests\nr = requests.post('http://flask:8000/default', 'http://nvie.com')\nprint(r.content)" | python3
