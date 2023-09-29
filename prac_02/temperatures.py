"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""
MENU = "C-Convert Celcius to Fahrenheit, F-Convert Fahrenheit to Celcius, Q-Quit"


def main():
    """Convert celcius to fahrenheit and vice versa."""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celcius = float(input("celcius: "))
            fahrenheit = convert_celcius_to_fahrenheit(celcius)
            print(f"Result: {fahrenheit:.2f} F")
        elif choice == "F":
            fahrenheit = float(input("fahrenheit: "))
            celcius = convert_fahrenheit_to_celcius(fahrenheit)
            print(f"Result: {celcius:.2f} C")
        # Hint: celcius = 5 / 9 * (fahrenheit - 32)
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def convert_celcius_to_fahrenheit(celcius):
    """Convert celsius to fahrenheit."""
    return celcius * 9.0 / 5 + 32


def convert_fahrenheit_to_celcius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5 / 9.0


main()
