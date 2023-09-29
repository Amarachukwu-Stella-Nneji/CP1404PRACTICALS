"""
display menu
get choice
while choice != quit option
    if choice == first option
        do first task
    else if choice == <second option>
        do second task
    ...
    else if choice == <n-th option>
        do n-th task
    else
        display invalid input error message
    display menu
    get choice
do final thing, if needed
"""
CHOOSE = "(H)ello\n(G)oodbye\n(Q)uit"
name = input("Enter your name: ").title()
print(CHOOSE)
users_choice = input("Choose : ").title()
while users_choice != "Q":
    if users_choice == "H":
        print(f"Hello, {name}!")
    elif users_choice == "G":
        print(f"Goodbye, {name}!")
    else:
        print("Invalid users_choice.")
    print(CHOOSE)
    users_choice = input("Choose : ").upper()
print("Finished.")
