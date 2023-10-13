"""
Emails
Estimate: 1 hour
Actual: 45 minutes
"""


def main():
    name_to_email = {}
    email = input("Email: ")
    while email != "":
        name = extract_name_from_email(email)
        name_to_email[name] = email
        email = input("Email: ")
    for name, email in name_to_email.items():
        print("")
        print(f"{name} ({email})")


def extract_name_from_email(email):
    email = email.split("@")
    name = ' '.join(email[0].split('.')).title()
    choice = input(f'Is your name {name}? (Y/n) ').upper()
    if choice != "Y" and choice != "":
        name = input("Name: ")
    return name


main()
