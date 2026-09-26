import random

boy_name = input("Enter a boy's name: ")
girl_name = input("Enter a girl's name: ")

love_score = random.randint(1, 100)

if love_score > 70:
    print("Your love score is " + str(love_score) + "%, you are made for each other!")
elif love_score > 30 and love_score <= 70:
    print("Your love score is " + str(love_score) + "%, you are still good together.")
else:
    print("Your love score is " + str(love_score) + "%, you might want to work on your relationship.")