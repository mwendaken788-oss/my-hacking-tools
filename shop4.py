while True:
    print("\nWelcome to Ken's Duka!")
    print("1. Sugar - 200")
    print("2. Milk - 100")
    print("3. Bread - 80")
    print("4. Cooking Oil - 350")
    print("5. EXIT - Close Shop")

    choice = input("Choose 1-5: ")

    if choice == "5":
        print("Shop Closed! Goodnight Ken!")
        break

    if choice == "1":
        item = "Sugar"
        price = 200
    elif choice == "2":
        item = "Milk"
        price = 100
    elif choice == "3":
        item = "Bread"
        price = 80
    elif choice == "4":
        item = "Cooking Oil"
        price = 350
    else:
        print("Wrong choice!")
        continue

    balance = int(input("Your M-Pesa Balance: "))
    pin = input("Enter M-Pesa PIN: ")

    if pin == "2028" and balance >= price:
        print("----- RECEIPT -----")
        print("Item:", item)
        print("Price:", price)
        print("New Balance:", balance - price)
        print("Thank you! Next Customer!")
        print("-------------------")
    else:
        print("Payment Failed!")
