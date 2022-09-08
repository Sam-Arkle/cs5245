# Rewrite the following to remove the continue:
# x = 5
# while x > 0:
#     y = int(input())
#     if y == 25:
#         continue
#     x -= 1
#     print(f'x = {x}')

x = 5
while x > 0:
    y = int(input())
    if y != 25:
        x -= 1
        print(f'x = {x}')
