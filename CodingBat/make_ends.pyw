Python 3.2.2 (default, Sep  4 2011, 09:51:08) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def make_ends(numbers):
	return [numbers[0], numbers[-1]]

>>> make_ends([1,2,3])
[1, 3]
>>> make_ends([1,2,3,4])
[1, 4]
>>> make_ends([7,4,6,2])
[7, 2]
>>> make_ends([13,28,3])
[13, 3]
>>> 
