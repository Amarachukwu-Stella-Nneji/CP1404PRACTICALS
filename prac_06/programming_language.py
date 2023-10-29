"""
programming_language.py
Estimate: 1 hour
Actual: 45 minutes
"""


class ProgrammingLanguage:
    """Compare programming language data."""

    def __init__(self, name, typing="", reflection=False, year=0):
        """Initialise programming language instance."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Returns True or False if the programming language is dynamically typed or not."""
        return self.typing == "Dynamic"

    def __str__(self):
        """Return string of name, typing, reflection and first appearance."""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"
