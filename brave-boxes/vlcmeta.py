#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
 
import sys, urllib2
from xml.dom.minidom import parseString

try:
    tagname = sys.argv[1]
    file = urllib2.urlopen('http://127.0.0.1:8080/requests/status.xml')
    data = file.read()
    file.close()
    dom = parseString(data)
    elementerinos = dom.getElementsByTagName(tagname)
    xmlData = "undefined"
    if len(sys.argv) == 2:
        xmlTag = elementerinos[0].toxml()
        xmlData = xmlTag.replace('<' + tagname+'>', '').replace('</' + tagname + '>', '')
        if sys.argv[1] == "position":
            xmlData = int(float(xmlData) * 100.0)
    else:
        for i in range(0, len(elementerinos) - 1):
            xmlTag = elementerinos[i].toxml()
            if "name=\"" + sys.argv[2] in xmlTag:
                xmlData = xmlTag.replace('<' + tagname + ' name=\"' + sys.argv[2] + '\">', '').replace('</' + tagname + '>', '')
    print xmlData
except:
    print "error"
