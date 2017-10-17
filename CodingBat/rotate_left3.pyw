Python 3.2.2 (default, Sep  4 2011, 09:51:08) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def rotate_left3(numbers):
	return [numbers[1], numbers[2], numbers[0]]

>>> rotate_left3([1,2,3])
[2, 3, 1]
>>> rotate_left3([5,11,9])
[11, 9, 5]
>>> rotate_left3([7,0,0])
[0, 0, 7]
>>> rotate_left3([3,13,28])
[13, 28, 3]
>>> 
