"""
CP1404 practical module
"""


class Project:
    """Contains project objects"""

    def __init__(self, name="", start_date="", priority=0, estimate=0.0, completion=0):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.estimate = estimate
        self.completion = completion

    def __str__(self):
        return f"{self.name}, start: {self.start_date}, priority {self.priority}, " \
               f"estimate: ${self.estimate:.2f}, completion: {self.completion}%"

    def __repr__(self):
        return f"{self.name}, {self.start_date}, {self.priority}, {self.estimate}, {self.completion}"

    def __lt__(self, other):
        return self.priority < other.priority

    def __gt__(self, other):
        return self.start_date > other.start_date

    def is_complete(self):
        return self.completion >= 100

    def is_incomplete(self):
        return int(self.completion) < 100

    def is_valid_percent(self):
        return int(self.completion) > 0 and self.completion.isint()
