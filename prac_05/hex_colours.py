COLOUR_TO_CODE = {"Absolute Zero": "#0048ba", "Acid Green": "#b0bf1a", "AliceBlue": "#f0f8ff",
                  "Alizarin crimson": "#e32636",
                  "Amaranth": "#e52b50", "Amber": "#ffbf00", "Amethyst": "#9966cc",
                  "AntiqueWhite": "#faebd7", "AntiqueWhite1": "#ffefdb", "AntiqueWhite2": "#eedfcc"}
for colour_name, code in COLOUR_TO_CODE.items():
    print(f"{colour_name} is {code}")
colour_name = input("Enter colour: ").lower()
if colour_name.lower() in (name.lower() for name in COLOUR_TO_CODE):
    for name, code in COLOUR_TO_CODE.items():
        if colour_name == name.lower():
            print(name, "is", code)
else:
    print("Invalid colour")
