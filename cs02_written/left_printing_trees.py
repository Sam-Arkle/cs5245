# Print a leftward facing tree of height specified by user

height = int(input("Enter the height of the tree: "))
for x in range(0, (2 * height)):
    if x <= height:
        print('{0:>{1}}'.format('*'*x, height))
    elif x > height:
        print('{0:>{1}}'.format('*' * (height-(x-height)), height))


# number of lines equals 2 * height -1. Top line is height - (height - 1) number of stars. And this increases by one
# until we get to height. At which point the # stars decreases from height down to 1
