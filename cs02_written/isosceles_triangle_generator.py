
height = int(input("Enter the height of the tree: "))
for x in range(1, 2 * height, 2):
    print('{0:^{1}}'.format('*' * x, 2 * height))
