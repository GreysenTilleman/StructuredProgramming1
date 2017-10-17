Python 3.2.2 (default, Sep  4 2011, 09:51:08) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from datetime import date
>>> first_date = date(2002, 9, 10)
>>> last_date = date(2017, 10, 6)
>>> delta = last_date - first_date
>>> print (delta.days)
5505
>>> 
