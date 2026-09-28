import datetime

date = datetime.date.today()

vehicles = {
    "bike": 500,
    "Car": 1500,
    "SUV": 2500,
    "Truck": 3500
}

rented_vehicles = []
vehicle_types = set()

print("=========== VEHICLE RENTAL SYSTEM ===========")
print("Date =", date)

while True:

    print("\n1. View Vehicles")
    print("2. Rent Vehicle")
    print("3. Return Vehicle")
    print("4. View Rental Summary")
    print("5. Exit")

    service = input("Enter your choice: ")

    
    if service == "1":

        print("\n------ Available Vehicles ------")

        for vehicle in vehicles:
            print(vehicle, "₹", vehicles[vehicle])


    elif service == "2":

        name = input("Enter the customer name: ")
        vehicle = input("Enter the type of vehicle you need: ")

        if vehicle in vehicles:

            days = int(input("Enter the number of days: "))

            cost = days * vehicles[vehicle]

            # Discount calculation

            if days >= 7:

                discount = cost * (20 / 100)
                final_price = cost - discount

            elif days >= 4:

                discount = cost * (10 / 100)
                final_price = cost - discount

            else:

                discount = 0
                final_price = cost


            rentals = {
                "Customer": name,
                "Vehicle": vehicle,
                "Days": days,
                "Cost": final_price
            }

            rented_vehicles.append(rentals)
            vehicle_types.add(vehicle)

            print("\nRental Successful!")
            print("Customer:", name)
            print("Vehicle:", vehicle)
            print("Days:", days)
            print("Original Price: ₹", cost)
            print("Discount: ₹", discount)
            print("Final Price: ₹", final_price)

        else:

            print("Vehicle not found.")


    elif service == "3":

        name = input("Enter the customer name: ")
        vehicle = input("Enter vehicle type: ")

        found = False

        for rental in rented_vehicles:

            if rental["Customer"] == name and rental["Vehicle"] == vehicle:

                print("\nVehicle returned successfully!")
                print("Customer:", rental["Customer"])
                print("Vehicle:", rental["Vehicle"])

                rented_vehicles.remove(rental)

                found = True
                break

        if found == False:
            print("Rental not found.")
            print("Enter the correct customer name and vehicle.")

    elif service == "4":

        if len(rented_vehicles) == 0:

            print("No rentals yet.")

        else:

            print("\n=========== RENTAL SUMMARY ===========")

            print("Total rentals:", len(rented_vehicles))
            print("Vehicle types:", vehicle_types)

            total_revenue = sum(
                rental["Cost"] for rental in rented_vehicles
            )

            highest_rental = max(
                rental["Cost"] for rental in rented_vehicles
            )

            lowest_rental = min(
                rental["Cost"] for rental in rented_vehicles
            )

            print("Total revenue: ₹", total_revenue)
            print("Highest rental: ₹", highest_rental)
            print("Lowest rental: ₹", lowest_rental)

            print("\n------ Rental Details ------")

            for rental in rented_vehicles:

                print("Customer:", rental["Customer"])
                print("Vehicle:", rental["Vehicle"])
                print("Days:", rental["Days"])
                print("Cost: ₹", rental["Cost"])
                print("----------------------------")


    elif service == "5":

        print("\nThank you for using the Vehicle Rental System!")
        print("Date:", date)
        break


    else:

        print("Invalid choice. Please select 1 to 5.")