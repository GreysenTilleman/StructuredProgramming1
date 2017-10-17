Python 3.2.2 (default, Sep  4 2011, 09:51:08) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def alarm_clock(day, vacation):
  if not vacation:
    if 1 <= day <= 5:
      return '7:00'
    return '10:00'
  
  if 1 <= day <= 5:
    return '10:00'
  return 'off'

>>> alarm_clock(1,False)
'7:00'
>>> alarm_clock(5,False)
'7:00'
>>> alarm_clock(0,False)
'10:00'
>>> 
