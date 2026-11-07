import socket

print("--- DNS Lookup Tool ---")
domain = input("Enter a domain (e.g., github.com): ")

try:
    ip_address = socket.gethostbyname(domain)
    print(f"\nThe IP address for {domain} is: {ip_address}")
except socket.gaierror:
    print("Error: Could not resolve the domain. Please check the name and try again.")
except Exception as e:
    print(f"An error occurred: {e}")
