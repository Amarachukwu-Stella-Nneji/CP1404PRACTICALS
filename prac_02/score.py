"""
CP1404/CP5632 - Practical
Program to determine score status
"""

import random


def main():
    """get valid random_score and print the result."""
    score = random.randint(0, 100)
    print(f"Random_score: {score}")
    print(determine_category(score))


def determine_category(score):
    """Determine the category of a given score."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
