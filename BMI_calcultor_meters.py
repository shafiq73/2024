# Step 1: Get the user's height and weight
height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))

# Step 2: Calculate the BMI
bmi = weight / (height ** 2)

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