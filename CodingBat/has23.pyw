Python 3.2.2 (default, Sep  4 2011, 09:51:08) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def has23(numbers):
	return 2 in numbers or 3 in numbers

>>> has23([2,5])
True
>>> has23([4,3])
True
>>> has23([4,5])
False
>>> has23([13,28,3])
True
>>> 
