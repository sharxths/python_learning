name = input("Enter Account holder name : ")
ACno = int(input("Enter the account number : "))
PIN = int(input("Enter the PIN : "))
in_balance = int(input('Enter the intial balance : '))
if(PIN == 1234 ):
    account = {
    "name" : name,
    "account_number" : ACno,
    "balance" : in_balance,
}

    account_types = ("Savings", "Current")
    print(account_types[0])
    print(account_types[1])

    services = { "Withdraw", "Deposit","Balance Check"}
    print(services)
    services.add("loan")
    print(services)

    user_service = input("Enter the service you need : ")
    if(user_service == "Balance check"):
     print("Your current balance is : ₹", in_balance)
    elif(user_service == "Deposit"):
     deposit_amount = int(input("Enter the deposit amount : "))
     in_balance = in_balance + deposit_amount
     print("Amount added successfully")
     print("New Balance : ₹", in_balance)
    elif(user_service == "Withdraw"):
     withdraw_amount = int(input("Enter the withdrwal amount: "))
     if (withdraw_amount > in_balance) :
        print("insufficient balance")
     else:
        print("amount debited")
        in_balance = in_balance - withdraw_amount
        print("Remaining_Balance : ₹", in_balance)

else:
  print("Incorrect PIN")






