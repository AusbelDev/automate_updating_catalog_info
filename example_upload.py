#! /usr/bin/env python3

import requests

# * This exmaple shows how a file can be uploaded using the python requests module

url = "http://localhost/upload/"
with open("/usr/share/apache2/icons/icon.sheet.png", "rb") as opened:
    r = requests.post(url, files={"file": opened})
