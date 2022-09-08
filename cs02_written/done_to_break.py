# rewrite the following using break rather than a done variable

# done = False
# n, m = 0, 100
# while not done and n != m:
#     n = int(input())
#     if n < 0:
#         done = True
#     print(f'n = {n}')

n, m = 0, 100
while n != m:
    n = int(input())
    if n < 0:
        break
    print(f'n = {n}')
