## 1 program using zip() function and list() function, create a merged list of tuples from the two lists given

first=[1,2,3,4,5]
sec=['a','b','c','d','e']
re=list(zip(first,sec))
print(re)

## 2 create a range from 1 to 8. Then using zip, merge the given list and the range together to create a new list of tuples

range1=[1,2,3,4,5,6,7,8]
range2=[9,10,11,12,13,14,15,16,17]
tog=list(zip(range1,range2))
print("tuple is",tog)

## 3	Using sorted() function, sort the list in ascending order.

num=[81,78,26,98,5,13,56,88,89,9,43,67]
sort=sorted(num)
print(sort)

##  4 program using filter function, filter the even numbers so that only odd numbers are passed to the new list.

num=[81,78,26,98,5,13,56,88,89,9,43,67]
def add(a):
    if(a%2!=0):
      return a
    else:
        return 0
odd=list(filter(add,num))
print(odd)
