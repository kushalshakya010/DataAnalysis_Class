import random
print("welcome to the number guessing game")
comp_choice = random.randint(1, 100)
print(comp_choice)

attempt = 0
while attempt<5:
    user_choice = int(input("guess a number between 1 to 100: "))
    attempt += 1
    print("you have", 5-attempt, "attempts left")

    if (user_choice < comp_choice):
        print("Guess higher")
    elif (user_choice > comp_choice):
        print("Guess lower")
    else:
        print("Congrats, you guessed the correct number")
        break
else:
    print("you have exhausted all your attempts, the correct number was", comp_choice)