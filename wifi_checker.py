import socket

print("=== LEVEL 10 - WIFI SAFETY CHECKER ===")
print("Checking YOUR network...")

# 1. What is my phone name?
my_name = socket.gethostname()
print("My phone name:", my_name)

# 2. What is my IP?
try:
    my_ip = socket.gethostbyname(my_name)
    print("My IP:", my_ip)
except:
    print("Could not find IP")

# 3. Is internet working?
try:
    socket.create_connection(("8.8.8.8", 53), timeout=3)
    print("Internet: WORKING ✅")
except:
    print("Internet: NOT WORKING ❌")

# 4. Check common doors (ports) on my own phone
print("\nChecking my doors...")
for port in [21, 22, 80, 443, 8080]:
    s = socket.socket()
    s.settimeout(1)
    result = s.connect_ex(("127.0.0.1", port))
    if result == 0:
        print(f"Port {port}: OPEN - Be careful!")
    else:
        print(f"Port {port}: CLOSED - Safe")
    s.close()

print("\nDone! Level 10 Complete!")
