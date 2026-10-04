def add(a, b):
    return a + b


num1 = int(input("enter the first number: "))
num2 = int(input("enter the second number: "))

result = add(num1, num2)
new_result = result + 10
print("The sum of", num1, "and", num2, "is:", result)
print("The new result after adding 10 is:", new_result)