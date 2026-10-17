# Exercise 2 (dictionary):
# Create a dictionary for a student with name, age, and marks (a list of 3 numbers). 
# Print the name, then add a key "passed" that is True if the average mark is 40 or more. Then loop through the dictionary with .
# items() and print every key and value.


student = {
    "name":"kushal", 
    "age":24, 
    "marks": [89, 49,87]
    }
    

print("name of student:", student["name"])

average = sum(student["marks"]) / len(student["marks"])
student["passed"] = average >=40

print("/n Student details:")
for key, value in student.items():
    print(f"{key} : {value}")