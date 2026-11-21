milk_stock = 5
bread_stock = 8
total_money = 0

while True:
    print("--- KEN'S DUKA - WHITE HAT SHOP ---")
    print("1. Milk - 100 KES - Stock:", milk_stock)
    print("2. Bread - 80 KES - Stock:", bread_stock)
    print("3. Close Shop")
    choice = input("Choose: ")

    if choice == "1":
        if milk_stock == 0:
            print("SORRY! Milk OUT OF STOCK!")
        else:
            tries = 0
            while tries < 3:
                pin = input("Enter PIN: ")
                if pin == "2028":
                    print("Milk Sold!")
                    milk_stock = milk_stock - 1
                    total_money = total_money + 100
                    print("Milk left:", milk_stock)
                    break
                else:
                    tries = tries + 1
                    print("Wrong PIN! Tries left:", 3 - tries)
                    if tries == 3:
                        print("SHOP LOCKED! TOO MANY WRONG PINs!")
    elif choice == "2":
        if bread_stock == 0:
            print("SORRY! Bread OUT OF STOCK!")
        else:
            tries = 0
            while tries < 3:
                pin = input("Enter PIN: ")
                if pin == "2028":
                    print("Bread Sold!")
                    bread_stock = bread_stock - 1
                    total_money = total_money + 80
                    print("Bread left:", bread_stock)
                    break
                else:
                    tries = tries + 1
                    print("Wrong PIN! Tries left:", 3 - tries)
                    if tries == 3:
                        print("SHOP LOCKED! TOO MANY WRONG PINs!")
    elif choice == "3":
        print("Total Money:", total_money)
        break
