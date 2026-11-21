print("--- File Scanner ---")
file = open("secret.txt", "r")
data = file.read()
print(data)

if "password" in data:
    print("FOUND IT! This file has a password!")
else:
    print("No password here")
