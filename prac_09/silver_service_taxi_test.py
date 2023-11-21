from silver_service_taxi import SilverServiceTaxi


def main():
    """Test the SilverServiceTaxi class."""
    silver_taxi = SilverServiceTaxi("Silver Taxi", 100, 2)
    silver_taxi.drive(18)
    print(silver_taxi.get_fare())
    silver_service_taxi = SilverServiceTaxi("Fancy Taxi", 100, 2.37)
    silver_service_taxi.drive(70)
    print(silver_service_taxi.get_fare())
    silver_service_taxi.start_fare()
    silver_service_taxi.drive(50)
    print(silver_service_taxi.get_fare())
    print(f"Taxi: {silver_service_taxi}\nCurrent Fare: ${silver_service_taxi.get_fare()}")


main()
