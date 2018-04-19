#!/usr/bin/env python2
import os
import sys

#Taking arguments with error control
if len(sys.argv)<2 or len(sys.argv)>2:
    print "Arguments are wrong.\n" \
          "Correct usage: removeHfromxyz.py xyz_file"
    exit(0)
else:
    XyzFileName = sys.argv[1]

XyzWoHFileName = XyzFileName.split('.xyz')[0] + '_withoutH.xyz'

XyzData = open(XyzFileName,'r').readlines()
XyzCommentLine = XyzData[1]
XyzData = XyzData[2:]

XyzWoData = []
for line in XyzData:
	Hcheck = line.split()[0]
	if Hcheck!="H":
		XyzWoData.append(line)

XyzWoFile = open(XyzWoHFileName,"w")
XyzWoFile.write(str(len(XyzWoData))+"\n")
XyzWoFile.write(XyzCommentLine)
for elem in XyzWoData:
	XyzWoFile.write(elem)
XyzWoFile.close()