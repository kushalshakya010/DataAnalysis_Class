## ATM Program using If-Else Statements
bankBalance = 100000
pincode = 1234


print("Welcome to the ATM")

userPin = int(input("Please enter your pin: "))
if userPin == pincode:
    print("Pin accepted. You can proceed with your transactions.")

    choice = 0
    while choice != 4:
        print("Your current balance is:", bankBalance)
        print("1. Withdraw Money")
        print("2. Deposit Money")
        print("3. Check Balance")
        print("4. Exit")

        choice = int(input("Please select an option (1, 2, 3, or 4): "))

        if choice == 1:
            withdrawAmount = int(input("Enter the amount to withdraw: "))
            if withdrawAmount <= bankBalance:
                bankBalance -= withdrawAmount
                print("Withdrawal successful. Your new balance is:", bankBalance)
            else:
                print("Insufficient funds.")
    
        elif choice == 2:
            depositAmount = float(input("Enter the amount to deposit: "))
            bankBalance += depositAmount
            print("Deposit successful. Your new balance is:", bankBalance)
        
        elif choice == 3:
            print("Your current balance is:", bankBalance)
        
        elif choice == 4:
            print("Thank you for using the ATM.")
        
    else:
        print("Invalid option selected.")
