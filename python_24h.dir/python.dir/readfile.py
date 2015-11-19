#!/usr/bin/env python

import re
import sys

# ---------- function ----------
def readf():
    global blist

    f = open('test.file')
    lines = f.readlines()
    f.close()
    # print len(lines), "lines. \n"
    
    i = 0  ;  j = 0
    while True:
        if i >= len(lines): break
        blist.append(j)

        line1 = lines[i].strip()
        line2 = lines[i+1].strip()
        line3 = lines[i+2].strip()
        line4 = lines[i+3].strip()
        i = i + 5
        j = j + 1 
     

        fline = line1 + ' ' + line2 + ' ' + line3 + ' ' + line4
        alist.append([ line1, fline, [line1, line2, line3, line4] ])
        # alist.append([ line1, fline,  ])
        # adict[ line1 ] = [ line1, line2, line3, line4]

        # print ":", fline, ":"

# ---------- function ----------
def matches(s1):
    global blist 
    global mlist 

    mlist = []
    n = len(blist)
    i = 0 
    while i < n: 
        # print s1, ":", alist[i][1]
        j = blist[i]

        alow = alist[j][1].lower()
        blow = s1.lower()
        # print alow, ":", blow
        if alow.find( blow ) > 0: 
           mlist.append( j )

        i = i + 1
    # on exit, save to blist
    blist = mlist

# ---------- main ----------
nparms = len( sys.argv ) 
# print sys.argv[1]

alist = []
blist = []
mlist = []

readf()
# print alist[1][0], ":", alist[0][0], ":", alist[1][1], ":", alist[1][2][2]

i = 1
while i < nparms:
   print sys.argv[i]
   matches( sys.argv[i] )
   print mlist, blist
   print
   i = i + 1
   

# matches("MsG")
# print mlist, blist

