## 1 add +2 to each in a list

a=[1,2,3,4,5,6,7,8,9]
for i in a:
   i=i+2
   print(i)
   
## 2 program to get a pattern

a=int(input("Enter a number: "))
t=len(str(a))
for i in range(t,0,-1):
    for j in range(i,0,-1):
          print(j,end='')
    print()
    
 ## 3  fibonacci sequence
 
a=int(input("Enter a number: "))
count=0
n1=0
n2=1
while count < a:
       print(n1)
       t = n1 + n2
       n1 = n2
       n2 = t
       count += 1
    
 ## 4 armstrong number
    An armstrong number is number , in which sum of cube of digits of a number is equal to its number
    
a = int(input("Enter a number: "))
sum = 0
t= a
while t > 0:
  digit = t % 10
  sum=sum + digit ** 3.
  t= t// 10.
if( a == sum):
    print("The given number is armstrong")
else:
    print("The given number is not armstrong")   
    
## 5 multiplication table of 9

a=int(input("Enter the table "))
i=1
while(i<11):
     print( a, " x", i  ,"=", str(a*i))
     i=i+1
     
 ## 6 a number is positive or not
 
a=int(input("Enter a number : "))
if(a>0):
    print("The number is positive")
else:
    print("the number is negative")
    
    
 ## 7 convert number of days to ages
 
d=int(input("Enter the number of days: "))
a=d//365
print("The age is ",a)

## 8 Trigonometry problem using math function 

import math 
a = math.pi/6
print ("The value of sine of pi/6 is : ",end='') 
print (math.sin(a)) 
print ("The value of cosine of pi/6 is : ",end='') 
print (math.cos(a))
print ("The value of tangent of pi/6 is : ", end="") 
print (math.tan(a))
print ("The converted value from radians to degrees is : ", end="") 
print (math.degrees(a)) 
b=int(input("Enter the degree :"))
print ("The converted value from degrees to radians is : ", end="") 
print (math.radians(b)) 


## 9 calculator

print("Calculator")
print("1.Addition")
print("2.Substraction")
print("3.Multiplication")
print("4.Dividision")
ch=int(input("Enter Choice: "))
if ch==1:
    a=int(input("Enter addend:"))
    b=int(input("Enter addend:"))
    c=a+b
    print("Sum = ",c)
elif ch==2:
    a=int(input("Enter minuend :"))
    b=int(input("Enter subtrahend:"))
    c=a-b
    print("Difference = ",c)
elif  ch==3:
    a=int(input("Enter multiplier:"))
    b=int(input("Enter multiplicant:"))
    c=a*b
    print("Product = ",c)
elif ch==4:
    a=int(input("Enter divident:"))
    b=int(input("divisor:"))
    c=a//b
    r=a%b
    print("Quotient = ",c)
    print("Remainder = ",r)
else:
    print("Invalid choice")

