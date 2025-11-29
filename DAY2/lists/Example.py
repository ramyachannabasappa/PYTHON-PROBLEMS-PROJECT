# What is list in python??

#Collection of items(heterogeneous)

#ordered,Duplicated,Mutable,No sorting required

#Homogeneous list
numbers=[10,20,30,40]

#heterpgeneous list
mixed=[10,"name",10.5,False]

#Accesing elements in a list

print(numbers[0])  #using index

#last value
print(numbers[-1])

#slicing of a list
print(numbers[1:3])

#FUNCTIONS OF LIST

#1. Append()
# add value at the end in a list

numbers.append(80)
print(numbers)

#2.Insert() 
numbers.insert(2,100)
print("After insertion at position 2:",numbers)

#3. Remove()
numbers.remove(100)
print("after removing 100:",numbers)

#4. pop()
numbers.pop(2)
print("after removing index 2 from pop():",numbers)

#5.clear()
numbers.clear()
print("after clearing the list:",numbers)

