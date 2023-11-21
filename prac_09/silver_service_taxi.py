from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialised version of a Car that includes silver service."""
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi instance, based on parent class Taxi."""
        super().__init__(name, fuel)
        self.price_per_km *= fanciness

    def get_fare(self):
        """Return the price for the silver service trip including the flagfall."""
        return super().get_fare() + self.flagfall

    def __str__(self):
        """Return a string like a Car  with flagfall."""
        return super().__str__() + f" plus a flagfall of ${self.flagfall}"
