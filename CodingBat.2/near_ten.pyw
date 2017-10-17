Python 3.2.2 (default, Sep  4 2011, 09:51:08) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def near_ten(numbers):
	return 0 <= (numbers % 10) <= 2 or 8 <= (numbers % 10) <= 10
	return numbers % 10 in [0,1,2,8,9,10]

>>> near_ten(12)
True
>>> near_ten(17)
False
>>> near_ten(19)
True
>>> 
