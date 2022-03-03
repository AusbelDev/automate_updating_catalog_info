#! /usr/bin/env python3

from PIL import Image
import os

path = "/supplier-data/images/"

list = os.listdir(path)


for name in list:
    img = Image.open(name).convert("RGB")
    img = img.resize((600, 400))
    img.save(name + ".jpg", "JPEG")
    img.close()
