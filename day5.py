## 1  perform the instruction
def math():
   a=int(input("Enter the first number "))
   b=int(input("Enter the second number "))
   print("")
   print("Adding of two numbers is         "+ str(a+b) )        
   print("Subtraction of two numbers is    "+ str(a-b))    
   print("Division of two numbers is       "+ str(a//b))      
   print("Multiplication of two numbers is "+ str(a*b))

math()


## exercise 2

def covid(name,temp=98):
    print("Patient name is " + name + " and his body temperature is " + str(temp))
name=str(input("Enter the patient name "))
temp=int(input("Enter the temperature "))
covid(name,temp)
