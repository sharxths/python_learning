
import datetime
date = datetime.date.today()
name = input("Enter Account holder name : ")
ACno = int(input("Enter the account number : "))
PIN = int(input("Enter the PIN : "))

if(PIN == 1234 ):
    account = {
    "name" : name,
    "account_number" : ACno,
    "balance" : 10000,
}
    withdrawals = []
    deposits = []
    transaction_types = set()
    t = int(input("Enter the number of transactions you want to make : "))
    for i in range(1, t+1):
        print(f"\n Transaction {i}: ")

        #asking for transaction:
        action = input("Deposit or Withdraw : ").capitalize()


        if(action == "Deposit"):
            print(f"You chose to {action}")
            amount = int(input("Enter the amount You want to deposit : ₹"))
            print(f"You deposited the amount : ₹{amount}")
            account["balance"] = account["balance"] + amount
            print("Your current balance is : ₹",account["balance"] )
            deposits.append(amount)
            transaction_types.add(action)

        elif(action == "Withdraw"):
             print(f"You chose to {action}")
             amount = int(input("Enter the amount You want to Withdraw : ₹"))
             if (amount <= account["balance"]):
              print(f"You Withdrawn the amount : ₹{amount}")
              account["balance"] = account["balance"] - amount
              print(f"Your Current balance is : ₹", account["balance"])
              withdrawals.append(amount)
              transaction_types.add(action)

             else:
               print("Insufficient Balance")

else:
          print("You entered a wrong PIN")


print("========== SUMMARY ==========\n")

print("Total deposits : ₹", sum(deposits))
print("Total Withdrawals : ₹", sum(withdrawals))
print("Largest Tranction : ₹", sum(deposits + withdrawals))
print("Transaction types : ", transaction_types)
print("Your total balance is : ₹", account["balance"]) 
print("Date : ", date)






    
       