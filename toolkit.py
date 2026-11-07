import os

def show_menu():
    print("\n--- My Hacking Toolkit ---")
    print("1. Port Scanner")
    print("2. Link Extractor")
    print("3. Password Generator")
    print("4. IP Info Fetcher")
    print("5. DNS Lookup")
    print("6. Exit")
    print("--------------------------")

while True:
    show_menu()
    choice = input("Choose an option (1-6): ")

    if choice == '1':
        os.system('python port_scanner.py')
    elif choice == '2':
        os.system('python link_extractor.py')
    elif choice == '3':
        os.system('python passgen.py')
    elif choice == '4':
        os.system('python ip_info.py')
    elif choice == '5':
        os.system('python dns_lookup.py')
    elif choice == '6':
        print("Exiting toolkit. Goodbye!")
        break
    else:
        print("Invalid choice. Please choose a number from 1 to 6.")
