import socket

print("--- Port Scanner ---")
print("Scanning your own phone...")

target = "127.0.0.1"

ports = [21, 22, 80, 443, 8080]

for port in ports:
    s = socket.socket()
    s.settimeout(1)
    result = s.connect_ex((target, port))
    if result == 0:
        print(f"Port {port} is OPEN!")
    else:
        print(f"Port {port} is CLOSED")
    s.close()

print("Scan done!")
