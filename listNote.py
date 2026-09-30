### Creating a list
fruit = ["apple", "banana", "orange"]
print("List of fruits are: ", fruit)

# REPLACING THE VALUE OF INDEX 1
fruit[1] = "grape"
print("After changing the value of index 1: ", fruit)

#Append a new fruit to the list
print("APPEND kiwi in the list ")
fruit.append("kiwi")
print(fruit)

# Sorting the list
print(" SORTING the list ")
marks = [90, 80, 70, 60, 50]
print("Marks before sorting: ", str(marks))
marks.sort()
print("Sorted marks are: ", str(marks))

# Inserting a new fruit at index 1
fruit.insert(1, "dragon fruit")
print("After inserting dragon fruit at index 1: ", fruit)