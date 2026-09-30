firstdict = {
    "student_id" : 1,
    "name" : "kushal",
    "address" : "banepa"
}
seconddict = {
    "student_id" : 2,
    "name" : "prabal",
    "address" : "kathmandu"
}

print(seconddict["address"])


thirddict = {
    "student_id" : [3,4,5],
    "name" : ["sujan", "sabin", "sujal"],
    "address" : ["lalitpur", "bhaktapur", "kathmandu"]
}

#add new keyvalue pair in dictionary
thirddict["phone"] = ["9800000000", "9811111111", "9822222222"]
print(thirddict)

students={
    "s1": {"name": "kirito", "marks": 20},
    "s2": {"name": "asuna", "marks": 30},
    "s3": {"name": "leafa", "marks": 40}
}
print(students["s1"])