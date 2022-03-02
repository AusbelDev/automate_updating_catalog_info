from PIL import Image
import glob


path = ".\\images\\"

list = glob.glob(glob.escape(path) + "*")

for name in list:
    print(name.split("\\")[-1])


for name in list:
    img = Image.open(name).convert("RGB")
    img = img.rotate(-90).resize((128, 128))
    img.save(name + ".jpg", "JPEG")
