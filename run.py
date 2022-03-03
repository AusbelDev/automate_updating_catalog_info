#! /usr/bin/env python3

import os
import requests
import locale
import json

json_template = {"name": None, "weight": None, "description": None, "image_name": None}

path = "/supplier-data/descriptions/"
url = "http://localhost/fruits/"

descriptions_list = os.listdir(path)

for description in descriptions_list:
    with open(description, "r") as opened:
        lines = opened.readlines()
        json_template["name"] = lines[0]
        json_template["weight"] = locale.atoi(lines[1].strip(" lbs"))
        json_template["description"] = lines[2]
        json_template["image_name"] = description.strip(".txt") + ".jpg"
    upload = json.dump(json_template)
    r = requests.post(url, data=json_template)
