##  1 Creating lambda function multiply x argument with y argument

def func(y):
  return lambda x : x * y
result = func(6)
print(result(11))


def fun():
   return lambda x,y:(x*y)
result = fun()
print(result(4,5))


## 2 fibonacci series to n using lambda

def fibonacci(n):
   result = [0, 1]
   any(map(lambda _:result.append(sum(result[-2:])),
         range(2, n)))

   return result[:n]

print(fibonacci(5))


## 3 Python program that multiply each number of given list with a given number 

a=[1,2,3,4,5,6,7]
for i in range(0,6,1):
     b=lambda x : x+a[i]
     print(b(8) , end=" ")     

##  4 Python program to find numbers divisible by 9 from a list of numbers 

n = [81,12, 65, 54, 39,63, 109, 34, 21,]


result = list(filter(lambda x: (x % 9 == 0), n))
nresult = list(filter(lambda x: (x % 9 != 0), n))

print("Numbers divisible by 13 are",result)
print("Number not divisible by 13 are",nresult)


## 5 Python program to count the even numbers in a given list of integers 

n = [81,12, 65, 54, 39,63, 109, 34, 21,67,90,78,3,14,78]
result = list(filter(lambda x: (x % 2 == 0), n))
print("The even numbers in the list are",result)
a=len(result)
print("The number of even number in the list are",a)

