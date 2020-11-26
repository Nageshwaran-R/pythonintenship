# Task 1
n = int(input("Enter list size : "))
my_list = []
for i in range(n):
    item = int(input())
    my_list.append(item)
print(my_list)
# Add an item to list
item = int(input("Enter an item to add : "))
my_list.append(item)
print("list after adding item :", my_list)

# delete an item in list
deleted_item = my_list.pop(3)
print("list after deleting :", my_list)

# Store largest number from the list to variable
max_value = max(my_list)
print("Largest number = ", max_value)

# Store smallest number from the list to variable
min_value = min(my_list)
print("Smallest number = ", min_value)

# Task 2
my_tuple = (11, 13, 16, 15, 10)
print("reverse of tuple :", my_tuple[::-1])

# Task 3
my_tuple = (11, 13, 16, 15, 10)
print("My tuple :", my_tuple)
my_tuple = list(my_tuple)
print("tuple after converting to list is :", my_tuple)
