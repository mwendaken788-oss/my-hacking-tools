print("Welcome to Ken's Duka!")
print("1. Sugar - 200 (Stock: 10)")
print("2. Milk - 100 (Stock: 5)")
print("3. Bread - 80 (Stock: 8)")
print("4. Cooking Oil - 350 (Stock: 3)")

choice = input("Choose 1-4: ")

if choice == "1":
    item = "Sugar"
    price = 200
    stock = 10
elif choice == "2":
    item = "Milk"
    price = 100
    stock = 5
elif choice == "3":
    item = "Bread"
    price = 80
    stock = 8
elif choice == "4":
    item = "Cooking Oil"
    price = 350
    stock = 3
else:
    item = "Nothing"
    price = 0
    stock = 0

print("You chose:", item)

balance = int(input("Your M-Pesa Balance: "))
pin = input("Enter M-Pesa PIN: ")

if pin == "2028" and balance >= price and price > 0 and stock > 0:
    print("----- RECEIPT -----")
    print("Shop: Ken's Duka, Mitunguu")
    print("Item:", item)
    print("Price:", price)
    print("Old Balance:", balance)
    print("New Balance:", balance - price)
    print("Stock Left:", stock - 1)
    print("Thank you! Come Again!")
    print("-------------------")
else:
    print("Payment Failed!")
