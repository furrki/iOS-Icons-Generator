#!/usr/bin/python
import cv2
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", help="High Resolution Square Image")
parser.add_argument("-t", "--type", help="Is Only Icon(i) or AppIcon(ai)")
parser.add_argument("-n", "--name", help="Icon Name")
args = parser.parse_args()
fname = args.file
type = args.type

img = cv2.imread(fname, cv2.IMREAD_UNCHANGED)
if img is not None:
    if not os.path.exists("./outputs"):
        os.makedirs("./outputs")
    if type is not None and type == "i":
        name = args.name
        sizes = [(32,1),(32,2),(32,3)]
    else:
        name = "icon"
        sizes = [(20,1),(20,2),(20,3),(29,1),(29,2),(29,3),(40,1),(40,2),(40,3),(60,2),(60,3),(76,1),(76,2),(83.5,2),(1024,1024)]
    for size in sizes:
        cv2.imwrite("outputs/"+name+"-"+str(size[0])+"@"+str(size[1])+"x.png", cv2.resize(img,(int(size[0]*size[1]),int(size[0]*size[1]))))
