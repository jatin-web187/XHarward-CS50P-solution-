import sys
from PIL import Image,ImageOps
infile=sys.argv[1]
outfile=sys.argv[2]
if len(sys.argv)<3:
    sys.exit("Too few command-line arguments")
inName,inExtension=infile.split(".")
OutName,outExtension=outfile.split(".")
extensionType=["jpg","jepg","png"]
if inExtension.lower() and outExtension.lower() not in extensionType:
    sys.exit("Invalid output")
try:
    muppetPhoto=Image.open(infile)
    shirtPic=Image.open("shirt.png")
except FileNotFoundError:
    sys.exit("Input does not exist")
if inExtension!= outExtension:
    sys.exit("Input and output have different extensions")
shirtSize=shirtPic.size
muppet=ImageOps.fit(muppetPhoto,shirtSize)
muppet.paste(shirtPic, (0, 0), shirtPic)
muppet.save(outfile)
