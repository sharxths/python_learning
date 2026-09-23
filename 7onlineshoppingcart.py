
print("----------SHOPPING CART-----------\n")

import datetime
date = datetime.date.today()

products = {
    "Laptop" : 50000,
    "Mouse"   : 1000,
    "Keyboard" : 2000,
    "Headphones" : 4000
}

#Customer details
Name = input('Enter your name : ').strip()
Product = input('enter the product you want to buy : ').strip()
quantity = int(input('Enter the quantity of product : '))

print("CUSTOMER NAME : " ,Name.upper())
print("Product : " ,Product)
print("Quantity : ", quantity)



#existing of products
if(Product in products ):
    print("Price per item : ₹" ,products[Product])
    total_amount = products[Product]*quantity
    if(total_amount >= 50000):
        print("Discount = 15%")
        discounted_price = (total_amount*15)/100
        print(discounted_price)
        print("Total amount to be paid : ₹", total_amount - discounted_price)
    elif(total_amount > 20000):
            print("Discount = 10%")
            discounted_price = (total_amount*10)/100
            print(discounted_price)
            print("Total amount to be paid : ₹", total_amount - discounted_price)
    else:
            print("Total amount to be paid : ₹", total_amount)

   

else:
      print("Product is not avialible! ")

print("Date : " ,date)
print("=====THANK YOU=====")

            
    


