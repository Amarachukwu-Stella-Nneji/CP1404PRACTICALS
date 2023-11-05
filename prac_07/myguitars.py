from guitar import Guitar


def main():
    guitars = []
    in_file = open('guitars.csv', 'r')
    for line in in_file:
        parts = line.strip().split(',')
        guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
        guitars.append(guitar)
        guitars.sort()
    in_file.close()
    for guitar in guitars:
        print(f"{guitar.name} ({guitar.year}) : {guitar.cost:,.2f}")


main()
