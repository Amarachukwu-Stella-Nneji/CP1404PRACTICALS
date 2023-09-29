MENU = "(G)et a valid score, (P)rint score category, (S)how stars, (Q)uit"


def main():
    """Get valid score, print score category, print stars representing the number of score given and print a farewell
    message."""
    score = " "
    print("MENU: ")
    choice = input("choice:").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            if score == " ":
                print("enter a valid score first")
            else:
                determine_category(score)
        elif choice == "S":
            stars(score)
        else:
            print("invalid choice")
        print("MENU: ")
        choice = input("choice:").upper()
    print("Farewell")


def get_valid_score():
    """Get valid score."""
    score = int(input("score: "))
    while score < 0 or score > 100:
        print("invalid score")
        score = int(input("score: "))
    return score


def determine_category(score):
    """Determine the category of a given score."""
    if score < 0 or score > 100:
        print("Invalid score")
    elif score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Passable")
    else:
        print("Bad")


def stars(score):
    if score == " ":
        print("enter a valid score first")
    else:
        print("*" * score)


main()
