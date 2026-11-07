import socket

target = input("Enter target IP or domain (e.g., google.com): ")
print(f"Scanning common ports on {target}...")

ports = [21, 22, 80, 443, 8080]

for port in ports:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    result = s.connect_ex((target, port))
    
    if result == 0:
        print(f"Port {port} is OPEN")
    else:
        print(f"Port {port} is closed")
    s.close()
