#!/usr/bin/python
import cv2
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", help="High Resolution Square Image")
parser.add_argument("-t", "--type", help="Is Only Icon(i) or AppIcon(ai)")
args = parser.parse_args()
fname = args.file
type = args.type

img = cv2.imread(fname, cv2.IMREAD_UNCHANGED)
if img is not None:
    if not os.path.exists("./outputs"):
        os.makedirs("./outputs")
    if type is not None and type == "i":
        sizes = [32, 32*2, 32*3]
    else:
        sizes = [40, 60, 29*2, 29*3, 40*2, 40*3, 60*2, 60*3, 20, 40, 29*1, 29*2, 40, 40*2, 76, 76*2, 83.5*2, 1024]
    for size in sizes:
        cv2.imwrite("outputs/icon_"+str(size)+"x"+str(size)+".png", cv2.resize(img,(int(size),int(size))))
