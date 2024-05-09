#Print welcome message
print("Welcome to the Weight Calculator. This program converts from kilograms (kg) to pounds (lb).")

# Ask the user to input a weight in kilograms
while True:
    try:
        weight_kg = float(input("Please enter the weight in kilograms (kg): "))
        break
    except ValueError:
        print("Invalid input! Please enter a valid numeric value.")

# Convert kilograms to pounds
weight_pounds = weight_kg * 2.20462

# Output the converted weight to the user
print(f"The weight of {weight_kg} kg is equavalent to {weight_pounds} pounds (lb).")