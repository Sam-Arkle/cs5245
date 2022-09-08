height = int(input("Enter height in inches: "))
weight = int(input("Enter weight in pounds: "))
bmi_div_703 = weight / (height ** 2)
bmi = 703 * bmi_div_703
category = ''
if bmi < 18.5:
    category = "underweight"
elif 18.5 <= bmi < 25:
    category = 'healthy'
elif 25 <= bmi < 30:
    category = 'overweight'
elif 30 <= bmi:
    category = 'obese'
print(f'The BMI is {bmi:.1f} which is considered to be {category}.')
