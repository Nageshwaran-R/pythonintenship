## 1 a-zA-Z 1-9

import re
text = input("enter:")
reg = "([0-9a-zA-Z]+)"
match = re.match(reg,text)
if match != None:
    print("True")
else:
    print("False")
    
##  2  Python program that matches a word containing 'ab'.

import re
text = input("enter:")
reg = '\w*ab\w*'
match = re.match(reg,text)
if match != None:
    print("True")
else:
    print("False")
    
## 3 Python program to check for a number at the end of a word/sentence.

import re
text = input("enter:")
reg =re.search('[0-9]$',text)

if reg != None:
    print("True")
else:
    print("False")
    

## 4 a Python program to search the numbers (0-9) of length between 1 to 3 in a given string

import re
num=input("Enter : ")
results = re.finditer(r"([0-9]{1,3})",num )
print("Number of length 1 to 3")
for n in results:
     print(n.group(0))
	 
## 5 a Python program to match a string that contains only uppercase letters

import re
text = input("enter:")
reg = '^[A-Z]*$'
match = re.match(reg,text)
if match != None:
    print("True")
else:
    print("False")
    
