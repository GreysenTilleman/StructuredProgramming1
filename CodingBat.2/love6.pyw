Python 3.2.2 (default, Sep  4 2011, 09:51:08) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def love6(a, b):
	return a == 6 or b == 6 or (a + b) == 6 or (a - b) == 6

>>> love6(6,4)
True
>>> love6(4,5)
False
>>> love6(1,5)
True
>>> 
