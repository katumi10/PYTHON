# create list
fruits = ["Apple", "Banana", "Pawpaw", "Orange","Watermelon"]

#edit an element
fruits[2] = "Guava"

#display list
print(fruits)

#display selected list
print(fruits[0:3])

#display second element
print(fruits[1])

numbers = [1, 2, 3, 4, 5]
#Add a new element at the end of a list
numbers.append(10) #Add 10 to numbers [1, 2, 3, 4, 5, 10]

#Add an element at the beginning or middle of the list
numbers.insert(0, 2)#where 0 indicates the position and 2 the element

#remove items
numbers.remove(10)#[2,1, 2, 3, 4, 5]

#remove all items
numbers.clear() # returns []

#check if an element is in a list
print(2 in numbers)

#check how many items are in a list / lenght
print(len(numbers))
print(numbers)