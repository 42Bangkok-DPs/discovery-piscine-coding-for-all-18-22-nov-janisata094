first_number = input("Enter the first number:\n").strip()
second_number = input("Enter the second number:\n").strip()

try:
 
    first_number = int(first_number)
    second_number = int(second_number)

    result = first_number * second_number

    print(f"{first_number} x {second_number} = {result}")

    if result > 0:
        print("The result is positive.")
    elif result < 0:
        print("The result is negative.")
    else:
        print("The result is positive and negative.")  

except ValueError:
    print("That's not a valid number.")