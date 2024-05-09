#Print welcome message
print("Welcome to the Weight Calculator. This program converts from kilograms (kg) to pounds (lb).")

# Ask the user to input a weight in kilograms
weight_kg = float(input("Please enter the weight in kilograms (kg):"))

# Convert kilograms to pounds
weight_pounds = weight_kg * 2.20462

# Output the converted weight to the user
print("The weight in pounds (lb) is:", weight_pounds)