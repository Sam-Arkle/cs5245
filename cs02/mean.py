from random import random

n = int(input("Enter n: "))
sum_ = 0
for x in range(n):
    sum_ += random()
average = sum_ / n
print(f'The average of {n} trials is {average:.3f}.')
