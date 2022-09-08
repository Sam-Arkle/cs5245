from random import uniform

n = int(input("Enter n: "))
c = 0
for x in range(n):
    a, b = uniform(-1, 1), uniform(-1, 1)
    point = (a ** 2 + b ** 2) ** (1/2)
    if point <= 1:
        c += 1
pi_approx = 4 * c / n
print(f'After {n} trials, the approximation is pi = {pi_approx:.6f}.')

