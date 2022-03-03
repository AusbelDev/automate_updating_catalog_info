#! /usr/bin/env python3
import requests
import glob

path = "/supplier-data/images/"
url = "http://localhost/upload/"

list_jpgs = glob.glob(path + "*.jpg")

for img_name in list_jpgs:
    with open(img_name, "rb") as opened:
        r = requests.post(url, files={"file": opened})
