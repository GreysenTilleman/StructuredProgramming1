Python 3.2.2 (default, Sep  4 2011, 09:51:08) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> Filename = input("Input the Filename: ")
Input the Filename: My.Stuff
>>> f_extns = Filename.split(".")
>>> print ("The extension of the file is : " + repr(f_extns[-1]))
The extension of the file is : 'Stuff'
>>> 
