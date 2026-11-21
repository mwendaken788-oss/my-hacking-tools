print("Welcome to Ken's Duka!")
print("1. Sugar - 200")
print("2. Milk - 100")
print("3. Bread - 80")
print("4. Cooking Oil - 350")

choice = input("Choose 1-4: ")

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
    price = 0
    item = "Nothing"

print("You chose:", item, "Price:", price)

balance = int(input("Your M-Pesa Balance: "))
pin = input("Enter M-Pesa PIN: ")

if pin == "2028" and balance >= price and price > 0:
    print("Payment Successful! Take your", item)
    print("Your new balance is:", balance - price)
else:
    print("Payment Failed! Wrong PIN or Not Enough Money!")
