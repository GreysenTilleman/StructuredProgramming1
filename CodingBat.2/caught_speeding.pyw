Python 3.2.2 (default, Sep  4 2011, 09:51:08) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def caught_speeding(speed, is_birthday):
  if is_birthday:
    speed -= 5
     
  if speed <= 60:
      return 0
  if 60 < speed <= 80:
    return 1
  return 2

>>> caught_speeding(60,False)
0
>>> caught_speeding(65,False)
1
>>> caught_speeding(65,True)
0
>>> 
