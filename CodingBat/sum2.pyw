Python 3.2.2 (default, Sep  4 2011, 09:51:08) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def sum2(numbers):
	if len(numbers) == 0:
		return 0
	if len(numbers) == 1:
		return [1]
	return numbers[0] + numbers[1]

>>> sum2([1,2,3])
3
>>> sum2([1,1])
2
>>> sum2([1,1,1,1])
2
>>> sum2([3,13,28])
16
>>> 
