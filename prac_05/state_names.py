"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
print(CODE_TO_NAME)
valid_input = False
while not valid_input:
    state_code = input("Enter short state: ").upper()
    try:
        state_name = CODE_TO_NAME[state_code]
        print(state_code, "is", state_name)
        valid_input = True
    except KeyError:
        print("Invalid short state")
