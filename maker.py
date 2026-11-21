print("I am making 100 passwords for you...")
name="john"
year="2005"
f=open("passwords.txt","w")
f.write(name+"\n")
f.write(name+year+"\n")
f.write(name+"123\n")
f.write("123456\n")
f.write("password\n")
f.write("qwerty\n")
for i in range(90):
    f.write(f"{name}{i}\n")
f.close()
print("Done! I made 100 passwords in passwords.txt")
