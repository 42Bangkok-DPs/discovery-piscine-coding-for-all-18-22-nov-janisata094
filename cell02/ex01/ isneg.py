number = input("Please enter a number: ").strip()
try:
    number = int(number)
    if number < 0:
        print("This number is negative.")
    elif number > 0:
        print("This number is positive.")
    else:
        print("This number is both positive and negative.")
except ValueError:
    
    print("That's not a valid number.")