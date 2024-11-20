number = input("Please enter a number: ").strip()
try:
    number = int(number)
    if number == 0:
        print("This number is equal to zero.")
    else:
        print("This number is different from zero.")
except ValueError:
    
    print("That's not a valid number.")