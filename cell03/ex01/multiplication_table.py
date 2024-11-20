number = input("Enter a number\n").strip()
try:
    number = int(number)  
    for i in range(10):
        print(f"{i} x {number} = {i * number}") 
except ValueError:
    print("That's not a valid number.")