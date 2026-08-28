def menu():
    print("\n--- banking system ---")
    print("1. check_balance")
    print("2. .deposit")
    print("3. .Withdraw")
    print("4. Exit")

balance = 0

while True:
    menu()
    chioce=int(input("enter your chioce(1-4): "))
    if chioce==1:
        print("your balance is:",balance)

    elif chioce==2:
        amount=int(input("enter your deposit amount: "))
        balance+=amount
        print("deposit successful! your new balenece is: ",balance)

    elif chioce==3:
        amount=(int(input("enter your withdraw amount:")))
        if amount>balance:
            print("insufficient balence! your current balance is: ", balance)

        else:
            balance-=amount
            print("withdraw successful! your new balance is:",balance)

    elif chioce==4:
        print("...thank you for using the banking system...")
        break
    else:
        print("invalid choice! please select between (1-4)")
    