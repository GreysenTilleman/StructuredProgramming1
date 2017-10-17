Python 3.2.2 (default, Sep  4 2011, 09:51:08) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> values = input("Enter a series of numbers separated by a comma ")
Enter a series of numbers separated by a comma 1, 2, 3, 4, 5
>>> list = values.split(",")
>>> tuple = tuple(list)
>>> print('List : ', list)
List :  ['1', '2', '3', '4', '5']
>>> print('Tuple : ',tuple)
Tuple :  ('1', '2', '3', '4', '5')
