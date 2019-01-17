#!/usr/bin/python
import cv2
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", help="High Resolution Square Image")
args = parser.parse_args()
fname = args.file

img = cv2.imread(fname)
if img is not None:
    print("OK img")
