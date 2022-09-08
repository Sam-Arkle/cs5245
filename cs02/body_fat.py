sex = input("Enter sex (M or F): ")
bfp = int(input("Enter body fat percentage: "))
classification = ''
if sex == 'M':
    if 2 > bfp:
        classification = "Deficient"
    elif 2 <= bfp <= 5:
        classification = "Essential fat"
    elif 6 <= bfp <= 13:
        classification = "Athletes"
    elif 14 <= bfp <= 17:
        classification = "Fitness"
    elif 18 <= bfp <= 24:
        classification = "Average"
    elif 25 <= bfp:
        classification = "Obese"
elif sex == 'F':
    if 10 > bfp:
        classification = "Deficient"
    elif 10 <= bfp <= 13:
        classification = "Essential fat"
    elif 14 <= bfp <= 20:
        classification = "Athletes"
    elif 21 <= bfp <= 24:
        classification = "Fitness"
    elif 25 <= bfp <= 31:
        classification = "Average"
    elif 32 <= bfp:
        classification = "Obese"
print(f'{bfp:.1f}% body fat for a {sex} is considered {classification}.')
