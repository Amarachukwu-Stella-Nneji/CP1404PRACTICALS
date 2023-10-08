numbers = []
for i in range(5):
    number = float(input("Number: "))  # Convert input to a float to handle decimal numbers
    numbers.append(number)
# Calculate the required information
first_number = numbers[0]
last_number = numbers[-1]
smallest_number = min(numbers)
largest_number = max(numbers)
average = sum(numbers) / len(numbers)
# Display the required information
print(f"The first number is {first_number}")
print(f"The last number is {last_number}")
print(f"The smallest number is {smallest_number}")
print(f"The largest number is {largest_number}")
print(f"The average of the numbers is {average:.1f}")


USERNAMES = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
name = input("Enter your name: ")
if name in USERNAMES:
    print("Access granted.")
else:
    print("Access denied.")
