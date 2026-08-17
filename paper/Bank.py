accounts = {
    "A001":{"name": "john", "balance": 5000},
    "A002" :{"name":"Sara", "balance":8000 }
}

transactions = []

while True:
    print("---ATM Menu---")
    print("1. Check balance")
    print("2. Deposit")
    print("3. withdraw")
    print("4. View transactions")
    print("5. Exit")

    choice = input("Enter your choice : ")

    if choice == "6":
        print("Thank you !")
        break

    account_ID = input("Enter your Account Id : ")

    if account_ID not in accounts:
        print("Invalid Accounts")
        continue
    accounts = accounts[account_ID]

    if choice == "1":
        print=(f"balace : {accounts('balance')}")

    if choice == "3":
        amount = float(input("Deposite Amount : "))


    if choice == "4":
        print("4")

    if choice == "5":
        print("5")

        
    