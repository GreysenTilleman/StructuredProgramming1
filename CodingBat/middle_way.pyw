Python 3.2.2 (default, Sep  4 2011, 09:51:08) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def middle_way(a, b):
	return [a[1], b[1]]

>>> middle_way([1,2,3],[4,5,6])
[2, 5]
>>> middle_way([7,7,7],[3,8,0])
[7, 8]
>>> middle_way([5,2,9],[1,4,5])
[2, 4]
>>> middle_way([28,13,3],[13,3,28])
[13, 3]
>>> 
