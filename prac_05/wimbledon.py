"""
wimbledon
Estimate: 1 hour
Actual: 1 hour
"""

import csv


def main():
    """Take a list of Wimbledon final matches and display the winners and their countries."""
    champion_to_wins = {}
    wimbledon_finals = []
    get_winners(wimbledon_finals)
    winning_countries = compile_winners(champion_to_wins, wimbledon_finals)
    display_winners(champion_to_wins, winning_countries)


def get_winners(wimbledon_finals):
    """Get winners data."""
    with open("wimbledon.csv", "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        rows = csv.reader(in_file)
        for row in rows:
            wimbledon_finals.append(row)


def compile_winners(champion_to_wins, wimbledon_finals):
    """Compile winners data."""
    countries = []
    for match in wimbledon_finals:
        try:
            countries.append(match[1])
            champion_to_wins[match[2]] += 1
        except KeyError:
            champion_to_wins[match[2]] = 1
    return set(countries)


def display_winners(champion_to_wins, winning_countries):
    """Take a dictionary of winners and a list of winning countries and display formatted"""
    print("Wimbledon Champions:")
    for champion, win in champion_to_wins.items():
        print(f"{champion} : {win}")
    print(f"These {len(winning_countries)} countries have won Wimbledon:")
    print(", ".join(country for country in sorted(winning_countries)))


main()
