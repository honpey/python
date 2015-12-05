#!/usr/bin/python
from matplotlib.pyplot import figure, show, gca
import numpy as np
import time
import os
import sys
import re

di={};
def	print_hello(name, age=18, province="shandong"):
	for i in range(0, 50):
		print i,
	print
	return name,age,province

if __name__ == "__main__":
	print "hello world"
	cell = print_hello("houpengyang",12,"beijing");
	name, age, province = print_hello("houpengyang",12,"beijing");
	print "---------------"
	print cell[0],cell[1],cell[2]
	print "---------------"
	print name
	print age+1
	print province
	print "-----------"
	print "type(di):",type(di)
	di["[. */"]="beijing";
	di["]. *\\"]="nanjing";

	for key in di:
		print key,di[key]
	
