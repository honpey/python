#!/usr/bin/python
import time
import os
import sys
import re

f = open("./hi")
numbers={}
numbers2=[]
line = f.readline()
while line:
#	print line,
#	content=line.split(';|:',2)[1] # re module 
	temp = re.split(';|:',line)
	temp[1]=temp[1].strip()
	print "TEMP:|",temp[1],"|",
	numbers.setdefault(temp[1],3)
	numbers2.append(temp[1])
	line = f.readline()
#print numbers
f.close
print "--------"
print numbers
print numbers2
numbers.clear()
numbers2=[]
print "--------"
print numbers
print numbers2

def foo():
	print "nihao"
if __name__=='__main__':
	print "main.."
	foo()

