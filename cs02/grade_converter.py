score = float(input("Enter the score: "))
grade = ''
if score > 100 or score < 0:
    grade = 'invalid'
elif 90 <= score <= 100:
    grade = 'A'
elif 80 <= score < 90:
    grade = 'B'
elif 70 <= score < 80:
    grade = 'C'
elif 60 <= score < 70:
    grade = 'D'
else:
    grade = 'F'
print(f'The score is {score} and the letter grade is {grade}.')
