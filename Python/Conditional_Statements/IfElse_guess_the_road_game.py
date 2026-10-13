input1 = input("do u want to choose door A or B: ").lower()
if input1 == "a":
    input2 = input("u passed 1st stage, now do u want to wait or swim: ").lower()
    if input2 == "wait":
        input3 = input("Congrats, a door has opened, now there are 2 doors, do u want to choose door A or B: ").lower()
        if input3 == "a":
            input4 = input("u passed 2nd stage, choose BLUE, GREEN or BLACK box: ").lower()
            if input4 == "black":
                print("Congrats, u won the game")
            else:
                print("u fell into a trap, game over")
        else:
            print("u fell into a trap, game over")
    else:
        print("u fell into a trap, game over")
else: 
    print("u fell into a trap, game over")
