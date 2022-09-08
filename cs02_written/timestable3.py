size = int(input("Please enter the table size: "))
for row in range(1, size + 1):
    for column in range(1, size + 1):
        product = row * column
        # if product % 2 == 0:
        #     print('{:<5}'.format('Even'), end='')
        # else:
        #     print('{:<5}'.format('Odd'), end='')
        print('{0:6}'.format(product), end='')
    print()


