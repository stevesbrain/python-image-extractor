#!/usr/bin/python2

"""Extract JPG data from files"""
"""Designed intially for Android Thumbdata3 files"""
"""but will work on any file that contains JPG data within it"""

import argparse

parser = argparse.ArgumentParser(description='Name of the file to address')

parser.add_argument('--file', dest='FileName', type=str, help='Filename containing images to process')

args = parser.parse_args()

print args.FileName

f=open(args.FileName,'rb')
tdata = f.read()
f.close()

# The starting sequence is \xff\xd8 technically 
# but \xff\xd8\xff works better for not-only-jpegs resource files.
# The second \xff is just a beginning of next jpeg frame.
ss = '\xff\xd8\xff'
se = '\xff\xd9'

count = 0
start = 0
while True:
    x1 = tdata.find(ss,start)
    if x1 < 0:
        break
    x2 = tdata.find(se,x1)
    jpg = tdata[x1:x2+1]
    count += 1
    fname = 'extracted%d03.jpg' % (count)
    fw = open(fname,'wb')
    fw.write(jpg)
    fw.close()
    start = x2+2
