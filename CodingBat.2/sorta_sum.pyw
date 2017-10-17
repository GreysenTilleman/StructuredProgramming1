Python 3.2.2 (default, Sep  4 2011, 09:51:08) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def sorta_sum(a, b):
	if 10 <= a + b < 20:
		return 20
	return a + b

>>> sorta_sum(3,4)
7
>>> sorta_sum(9,4)
20
>>> sorta_sum(10,11)
21
>>> 
