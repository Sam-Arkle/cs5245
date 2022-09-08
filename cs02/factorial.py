n = int(input("Enter n: "))
product = 1
for x in range(1, n+1):
    # print(f'{x} x {product} = {product * x}')
    print(f'{x} x {product} = ', end='')
    product *= x
    print(product)
print(f'{n}! = {product}')
