Python 3.2.2 (default, Sep  4 2011, 09:51:08) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> i = int(input("Integer: "))
Integer: 13
>>> n1 = int( "%s" % i )
>>> n2 = int( "%s%s" % (i,i) )
>>> n3 = int( "%s%s%s" % (i,i,i) )
>>> print (n1+n2+n3)
132639
>>> 
