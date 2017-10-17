Python 3.2.2 (default, Sep  4 2011, 09:51:08) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def max_end3(numbers):
	M = max(numbers[0], numbers[2])
	return [M,M,M]

>>> max_end3([1,2,3])
[3, 3, 3]
>>> max_end3([11,5,9])
[11, 11, 11]
>>> max_end3([2,11,3])
[3, 3, 3]
>>> max_end3([13,28,3])
[13, 13, 13]
>>> 
