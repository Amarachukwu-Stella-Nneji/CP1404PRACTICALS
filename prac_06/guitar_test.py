"""
guitar_test
Estimate - 45 minutes
Actual - 30 minutes
"""

from prac_06.guitar import Guitar

gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
Fender = Guitar("Fender", 2014, 350)
print(f"{gibson.name} get_age() - Expected 101. got {gibson.get_age()}")
print(f"{Fender.name} get_age() - Expected 9. got {Fender.get_age()}")
print(f"{gibson.name} is_vintage() - Expected True. got {gibson.is_vintage()}")
print(f"{Fender.name} is_vintage() - Expected False. got {Fender.is_vintage()}")
