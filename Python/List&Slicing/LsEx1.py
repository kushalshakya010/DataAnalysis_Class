# Exercise 1 (lists and slicing):
# Given marks = [45, 78, 32, 90, 67, 55, 88], 
# print: the first three marks, the last two marks, every second mark, and the average (use sum and len).

marks = [45, 78, 32, 90, 67, 55, 88]

print(marks[:3])
print(marks[-3:])
print(marks[::2])

total = sum(marks)
print(total)
average = total / len(marks)
print(average)