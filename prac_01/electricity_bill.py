TARIFF_11 = 0.244618
TARIFF_31 = 0.136928
tariff_choice = input("Which tariff? 11 or 31: ")
cents_per_kwh = 0
while tariff_choice != "11":
    if tariff_choice == "31":
        cents_per_kwh = TARIFF_31
    else:
        print("invalid input")
        tariff_choice = input("Which tariff? 11 or 31: ")
    cents_per_kwh = TARIFF_11
    daily_use_in_kwh = float(input("Enter daily use in kWh: "))
    number_of_billing_days = int(input("Enter number of billing days: "))
    estimated_bill = (cents_per_kwh * daily_use_in_kwh) * number_of_billing_days / 100  # Convert cents to dollars
    print(f"Estimated bill: ${estimated_bill:.2f}")
