milk_stock = 5
bread_stock = 8
total_money = 0
my_pin = "2028"

while True:
    print("--- KEN'S DUKA - LEVEL 2 ---")
    print("1. Milk - 100 KES - Stock:", milk_stock)
    print("2. Bread - 80 KES - Stock:", bread_stock)
    print("3. Close Shop")
    print("4. Forgot PIN?")
    choice = input("Choose: ")

    if choice == "1":
        if milk_stock == 0:
            print("SORRY! Milk OUT OF STOCK!")
        else:
            tries = 0
            while tries < 3:
                pin = input("Enter PIN: ")
                if pin == my_pin:
                    print("Milk Sold!")
                    milk_stock = milk_stock - 1
                    total_money = total_money + 100
                    print("Milk left:", milk_stock)
                    break
                else:
                    tries = tries + 1
                    print("Wrong PIN! Tries left:", 3 - tries)
                    if tries == 3:
                        print("SHOP LOCKED!")
    elif choice == "2":
        if bread_stock == 0:
            print("SORRY! Bread OUT OF STOCK!")
        else:
            tries = 0
            while tries < 3:
                pin = input("Enter PIN: ")
                if pin == my_pin:
                    print("Bread Sold!")
                    bread_stock = bread_stock - 1
                    total_money = total_money + 80
                    print("Bread left:", bread_stock)
                    break
                else:
                    tries = tries + 1
                    print("Wrong PIN! Tries left:", 3 - tries)
                    if tries == 3:
                        print("SHOP LOCKED!")
    elif choice == "3":
        print("Total Money:", total_money)
        break
    elif choice == "4":
        print("SECRET CHECK!")
        ans = input("What town are you from? ")
        if ans == "Mitunguu":
            print("Correct! Your PIN is:", my_pin)
        else:
            print("WRONG! You are NOT the owner! GO AWAY THIEF!")
