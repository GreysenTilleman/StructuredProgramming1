Python 3.2.2 (default, Sep  4 2011, 09:51:08) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def in1to10(n, outside_mode):
	if not outside_mode:
		return n in range(1,11)
	return n <= 1 or n >= 10

>>> in1to10(5,False)
True
>>> in1to10(11,False)
False
>>> in1to10(11,True)
True
>>> 
