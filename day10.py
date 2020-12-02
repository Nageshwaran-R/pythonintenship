## 1 a-zA-Z 1-9

import re
text = input("enter:")
reg = "([0-9a-zA-Z]+)"
match = re.match(reg,text)
if match != None:
    print("True")
else:
    print("False")
    
##  Python program that matches a word containing 'ab'.

import re
text = input("enter:")
reg = '\w*ab\w*'
match = re.match(reg,text)
if match != None:
    print("True")
else:
    print("False")
    
## a Python program to check for a number at the end of a word/sentence.
