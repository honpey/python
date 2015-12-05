#!/usr/bin/python
print "Hello,World"
#raw_input("Press enter key to close this window");
classmates=["hello", "nihao", "ni"];
print classmates
print len(classmates)
classmates.append("xiaoming");
classmates.append("xiaohong");
print classmates
classmates.insert(1,"xiaoliang");
print classmates
classmates[1]="xiaoliangliang";
print classmates

age = "20"
if age > 18:
	print age
else:
	print "less than 18"

sum = 0;
for i in range(1,5):
	print i
	sum += i;
print "------------"
print sum

dict={"a":2, "b":3}
print dict
dict.append(1:"hello");
print dict[1]
