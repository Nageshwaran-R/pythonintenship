## 1 Try Exception

try:
 print(y)
except SyntaxError:
 print("Variable is not defined")


x=3
y=0
try: 
    result = x // y 
    print("quotient ", result) 
except ZeroDivisionError: 
    print("Sorry ! You are dividing by zero ") 
  
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")
  
  
 try:
  print(y)
except:
  print("variable is not defined")
finally:
  print("The error is finished")
  
 x = 109

if (x % 10 = 0) 
  raise ValueError("Only integers are allowed")

    
 ## 2 calcutor with try except
 
a = int(input("Enter a number"))
b = int(input("Enter a number"))
print("What you like to perform")
print("1.add")
print("2.subtract")
print("3.divide")
print("4.multiply")
ch=int(input("Enter the choice"))
if(ch==1):
     add()
elif(ch==2):
    sub()
elif(ch==3):
     div()
elif(ch==4):
     mul()
else:
    print("Enter a valid option")
    
def add():
  try:
      answer = a + b
      print(answer)
  except ValueError:
      print("float type error")
def sub():
  try: 
    answer = a - b
    print(answer)
  except ValueError:
    print("Invalid number")

def div():
    try:
     answer = a // b
     print(answer)
    except ZeroDivisionError:
     print("Number is not divisible by zero")

def mul():
    try: 
     answer = a * b
     print(answer)
    except ValueError:
        prin("Invalid content")
      
      
## 	print one message if the try block raises a NameError and another for other errors

a=int(input("Enter a number ")
b=int(input("Enter a number ")
try:
       c= a // b
       print(d)
except NameError:
       print(Enter a correct variable")
             
try:
       c = a// b
       print(c)
except ZeroDivisionError:
        print("the number is not divisible by 0")
             
             
## when try block is not used
             
print(" In my thoought, A try except is not used when a program doesnot have any error in it..")
             
             
## getting an input inside the try catch block
             
a=int(input("WEnyter a number"))
try:
   b=int(input("Enter the second number "))
   c= a//b
   print("c")
except ZeroDivisionError:
   print("Zero divisible error")
   print("Enter a number other than 0")
   b=int(input("Enter the correct number "))
   c=a//b
   print(c)
             
             
            
             
       
       
       
 

