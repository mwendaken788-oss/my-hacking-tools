password = input("Enter password: ")
score = 0
if len(password) >= 8:
    score += 1
    print(" Length ok")
else:
    print("Too short")
if any(c.isupper() for c in password):
    score += 1
    print("Has UPPERCASE")
if any(c.isdigit() for c in password):
    score += 1
    print("Has number")
if any(c in "!@#$%" for c in password):
    score += 1
    print("Has symbol")
print(f"score:{score}/4")
