weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))
bmi = weight / (height ** 2)

if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif 18.5 <= bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif 25 <= bmi < 30:
    print(f"Your BMI is {bmi}, you are overweight.")
else:
    print(f"Your BMI is {bmi}, you are obese.")