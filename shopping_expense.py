import datetime
print("========== SHOPPING EXPENSE TRACKER =========")
products = {
    "Milk": 30,
    "Bread": 40,
    "Eggs": 70,
    "Rice": 80,
    "Apples": 120
}
cart = []

date = datetime.date.today()
print("Date : " ,date)
input("Enter your name: ")

for product in products:
    print("Avialible Items")
    print(products, "₹", products[product])
    item = input("Enter the item you want to buy: ")
    if item in products:
      print("Item is availible")
      quantity = int(input("Enter the quantity of item: "))
      bill = quantity*products[item]
      print("Total bill : ₹", bill)
      if bill>= 500:
         discount = bill*0.15
         print("Discount : ",discount)
         print("Final bill : ₹", bill - discount)
      elif bill >= 200:
         discount = bill*0.05
         print("Discount : ", discount)
         print("Final bill : ₹", bill - discount)
      else:
         print("Final bill : ₹", bill)

    else:
       print('Items are not avialible !')

    break
