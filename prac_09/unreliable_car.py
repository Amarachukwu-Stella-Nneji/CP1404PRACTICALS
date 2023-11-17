import random

from prac_09.car import Car


class UnreliableCar(Car):
    """Specialised version of a Car that includes reliability."""

    def __init__(self, name, fuel, reliability):
        """Initialise a UnreliableCar instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive a given distance depending on the reliability."""
        if random.uniform(0, 100) < self.reliability:
            return super().drive(distance)
        else:
            return 0
