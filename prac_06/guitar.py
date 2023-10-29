"""
guitar.py
Estimate - 45 minutes
Actual - 30 minutes
"""

CURRENT_YEAR = 2023
VINTAGE_AGE = 50


class Guitar:
    """Represent a guitar object."""

    def __init__(self, name="", year=0, cost=0):
        """Initialise a guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return name, year and cost."""
        return f"{self.name} ({self.year}) : ${self.cost:.2f}"

    def get_age(self):
        """Returns how old the guitar is in years"""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Returns True if the guitar is 50 or more years old, otherwise False."""
        return self.get_age() > VINTAGE_AGE
