# Step 1: Get the user's height and weight
height_feet = int(input("Enter your height in feet: "))
height_inches = int(input("Enter your height in inches (in addition to the feet): "))
weight = float(input("Enter your weight in kilograms: "))

# Convert height from feet and inches to meters
height_meters = (height_feet * 0.3048) + (height_inches * 0.0254)

# Step 2: Calculate the BMI
bmi = weight / (height_meters ** 2)

# Step 3: Determine the BMI category
if bmi < 18.5:
    category = "Underweight"
elif bmi >= 18.5 and bmi < 25:
    category = "Normal weight"
elif bmi >= 25 and bmi < 30:
    category = "Overweight"
else:
    category = "Obese"

# Step 4: Print the results
print(f"Your BMI is: {bmi:.2f}")
print(f"You are considered {category}")