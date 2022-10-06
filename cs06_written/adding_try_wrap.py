# 8. Wrap with try:
# (a) Wrap the following code in a try statement to defend against any exceptions it can raise.
# Do not use a catch-all handler.
lst = [0, 0, 0, 0]
try:
    with open('data.txt', 'r') as f:
        count = 0
        for line in f.readlines():
            lst[count] = int(line)
            count += 1
except FileNotFoundError:
    print('File not found!')
except IndexError:
    print("You've hit an index error, make a bigger list next time")
