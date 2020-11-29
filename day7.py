## 1 module

module.py
 a=["apple","Grape","pineapple","orange"]
 
task.py
 import module
 module.a.append("peach","green apple")
 print(module.a)
	
	
## pandas package

import pandas as pd
import numpy as np
s=pd.Series(["Nagesh","Ramesh","Suresh","Mukesh"])
print(s)
 
## 3 random number
 
from random import randint
for _ in range(1):
	value = randint(1,100)
	print(value)



## 4 print the path using sys

import sys
print(sys.path)

