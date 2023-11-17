from prac_09.unreliable_car import UnreliableCar


def main():
    """Test the unreliable car class."""
    limo = UnreliableCar("limo", 100, 100)
    limo.drive(10)
    print(limo)
    my_car = UnreliableCar("my_car", 100, 50)
    my_car.drive(10)
    print(my_car)
    jeep = UnreliableCar("Hummer", 100, 0)
    jeep.drive(10)
    print(jeep)


if __name__ == '__main__':
    main()
