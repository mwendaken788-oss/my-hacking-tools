print("--- Password Cracker ---")
print("Trying to crack Ken's password...")

real_password = "K3n@2028"

tries = ["1234", "password", "ken123", "qwerty", "K3n@2028", "letmein"]

for guess in tries:
    print("Trying:", guess)
    if guess == real_password:
        print("CRACKED! Password is:", guess)
        break
    else:
        print("Wrong, next...")
