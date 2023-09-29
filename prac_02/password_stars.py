MINIMUM_LENGTH = 5


def main():
    """Get and print valid password as asterisks"""
    password = input("Enter a password: ")
    password = get_password(password)
    print_asterisks(password)


def print_asterisks(password):
    """Print password as asterisks"""
    asterisks = '*' * len(password)
    print(f"Password: {asterisks}")


def get_password(password):
    """Get valid password"""
    while len(password) < MINIMUM_LENGTH:
        password = input("Enter a password: ")
    return password


main()
