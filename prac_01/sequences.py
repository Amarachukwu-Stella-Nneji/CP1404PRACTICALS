def show_even_numbers(x, y):
    print("Even numbers:")
    for i in range(x, y + 1):
        if i % 2 == 0:
            print(i, end=' ')


def show_odd_numbers(x, y):
    print("\nOdd numbers:")
    for i in range(x, y + 1):
        if i % 2 != 0:
            print(i, end=' ')


def show_squares(x, y):
    print("\nSquares:")
    for i in range(x, y + 1):
        print(i * i, end=' ')


x = int(input("Enter the start number (x): "))
y = int(input("Enter the end number (y): "))

while True:
    print("1. Show even numbers from x to y")
    print("2. Show odd numbers from x to y")
    print("3. Show squares of the numbers from x to y")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        show_even_numbers(x, y)
    elif choice == 2:
        show_odd_numbers(x, y)
    elif choice == 3:
        show_squares(x, y)
    elif choice == 4:
        print("goodbye")
    else:
        print("Invalid choice. Please try again.")
        choice = int(input("Enter your choice: "))

