print("Welcome to Ken's Duka!")

item = input("What do you want to buy? ")
price = int(input("Price of item: "))
balance = int(input("Your M-Pesa Balance: "))
pin = input("Enter M-Pesa PIN: ")

if pin == "2028" and balance >= price:
    print("Payment Successful! Take your", item)
    print("Your new balance is:", balance - price)
else:
    print("Payment Failed! Wrong PIN or Not Enough Money!")
