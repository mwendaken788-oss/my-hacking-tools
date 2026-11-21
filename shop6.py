milk_stock = 5
bread_stock = 8
total_items = 0
total_money = 0

while True:
    print("--- KEN'S DUKA ---")
    print("1. Milk - 100 KES - Stock:", milk_stock)
    print("2. Bread - 80 KES - Stock:", bread_stock)
    print("3. Close Shop")
    choice = input("Choose: ")

    if choice == "1":
        if milk_stock == 0:
            print("SORRY! Milk is OUT OF STOCK!")
        else:
            pin = input("Enter PIN: ")
            if pin == "2028":
                print("Milk Sold!")
                milk_stock = milk_stock - 1
                total_items = total_items + 1
                total_money = total_money + 100
                print("Milk left:", milk_stock)
            else:
                print("Wrong PIN!")
    elif choice == "2":
        if bread_stock == 0:
            print("SORRY! Bread is OUT OF STOCK!")
        else:
            pin = input("Enter PIN: ")
            if pin == "2028":
                print("Bread Sold!")
                bread_stock = bread_stock - 1
                total_items = total_items + 1
                total_money = total_money + 80
                print("Bread left:", bread_stock)
            else:
                print("Wrong PIN!")
    elif choice == "3":
        print("Total Items:", total_items)
        print("Total Money:", total_money)
        break
