number = input("Enter a number less than 25\n").strip()

try:
    number = int(number)
    
    if number > 25:
        print("Error")
    else:
        
        while number <= 25:
            print(f"Inside the loop, my variable is {number}")
            number += 1

except ValueError:
    print("That's not a valid number.")