#!/usr/bin/python
"""
We can not use range, because range make a list for 
[0,2147483674], All the 4G is reserved in RAM
"""
def main():
	pass
def rangeBitwiseAndRaw(m, n):
	num=0xffffffff;
	i = m;
	while i<=n:
		num &= i;
		i += 1;
	return num;

def rangeBitwiseAnd(m, n):
	i = 0
	while m != n:
		m >>= 1
		n >>= 1
		i += 1
	return n << i

if __name__ == "__main__":
	main()
	m=122284
	n=122293
	res = rangeBitwiseAndRaw(m, n)
	print res;
	res = rangeBitwiseAnd(m,n)
	print res;
