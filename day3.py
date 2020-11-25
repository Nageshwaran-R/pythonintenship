## 1 Python script to merge two Python dictionaries

opp1 = {"happy":"sad","laugh":"cry"}
opp2 = {"difficult":"easy","push":"pull"}
opp1.update(opp2)                                      ## joining two dictionaries
print(opp1)

## 2 Python program to remove a key from a dictionary

opp1={"happy":"sad","laugh":"cry","push":"pull"}
del opp1["happy"]                                      ## deleting a keyword
print(opp1)

## 3 Python program to map two lists into a dictionary

key={1,2,3,4,5}                                        ## list 1
values={"apple","orange","grape","pineapple","peach"}  ##list 2
fruits=dict(zip(key,values))                           ## adding two lists using zip function
print(fruits)

## 4 Python program to find the length of a set

fruits={"apple","orange","grape","pineapple","peach"}  ## list
r=len(fruits)                                          ## counting the lenth of set using len() function
print(r)

## 5 Python program to remove the intersection of a 2nd set from the 1st set

a={0,1,2,3,4}                                          ## 1 set
b={5,6,7,8,9}                                          ## 2 set
a.update(b)                                            ## joininh two sets
print(a)         
print(a-b)                                             ## removing the 2nd set from 1st set and printing 
