# 1
name = input("Enter your name: ")
with open("name.txt", "w") as out_file:
    out_file.write(name)
    out_file.close()

# 2
with open("name.txt", "r") as in_file:
    name = in_file.read()
in_file.close()
print("Your name is", name)

# 3
with open("numbers.txt", "r") as in_file:
    number1 = int(in_file.readline())
    number2 = int(in_file.readline())
    total = number1 + number2
in_file.close()
print("The sum of the first two numbers is:", total)

# 4
with open("numbers.txt", "r") as in_file:
    total = 0
    for line in in_file:
        number = int(line)
        total += number
in_file.close()
print(f"The sum of all numbers is {total}")
