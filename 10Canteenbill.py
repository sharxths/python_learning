import datetime

date = datetime.date.today()

menu = {
    "Idli": 30,
    "Dosa": 50,
    "Rice": 60,
    "Coffee": 20,
    "Tea": 15
}

ordered_items = set()

Name = input("Enter your name: ")

print("\n---------- MENU ----------")

for items in menu:
    print(items, "₹", menu[items])

Dish = input("Enter the dish you want: ")
quantity = int(input("Enter the quantity: "))

if Dish in menu:

    ordered_items.add(Dish)

    total_cost = menu[Dish] * quantity

    if total_cost >= 200:
        discount = total_cost * (10 / 100)
        final_bill = total_cost - discount

    elif total_cost >= 100:
        discount = total_cost * (5 / 100)
        final_bill = total_cost - discount

    else:
        discount = 0
        final_bill = total_cost

    print("\n---------- SUMMARY ----------")
    print("Date:", date)
    print("Customer Name:", Name)
    print("Dish Ordered:", Dish)
    print("Quantity:", quantity)
    print("Total Cost: ₹", total_cost)
    print("Discount: ₹", discount)
    print("Final Bill: ₹", final_bill)
    print("Ordered Items:", ordered_items)

else:
    print("Dish is not available.")