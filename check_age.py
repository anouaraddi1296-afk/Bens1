try:
    age = int(input("How old are you? "))
    if age >= 18:
        print("You are an adult. You can vote!")
    else:
        print("You are a minor. You cannot vote yet.")
except ValueError:
    print("Error: Please enter a valid number (like 20), not text!")
