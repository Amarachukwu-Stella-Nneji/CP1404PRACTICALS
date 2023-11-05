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

    guitar_name = input("New guitar: ")
    while guitar_name != "":
        guitar_year = input("Year: ")
        guitar_cost = float(input("Cost: $"))
        guitar = Guitar(guitar_name, int(guitar_year), float(guitar_cost))
        guitars.append(guitar)
        guitars.sort()
        guitar_name = input("New guitar: ")
        out_file = open('guitars.csv', 'w')
        for guitar in guitars:
            out_file.write(f"{guitar.name},{guitar.year},{guitar.cost}\n")
        out_file.close()


main()
