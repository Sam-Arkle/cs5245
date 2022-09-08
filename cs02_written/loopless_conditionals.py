# x, y, z = int(input("#1 ")), int(input("#2 ")), int(input("#3 "))
# maximum = 0
# if x < y or x < z:
#     if y < z:
#         maximum = z
#     else:
#         maximum = y
# else:
#     maximum = x
#
# print(f'The biggest number you could think of was {maximum}')
#

# Minimum below
# x, y, z = int(input("#1 ")), int(input("#2 ")), int(input("#3 "))
# minimum = 0
# if x > y or x > z:
#     if y > z:
#         minimum = z
#     else:
#         minimum = y
# else:
#     minimum = x
#
# print(f'The smallest number you could think of was {minimum}')

# (c) Write a Python program (without loops) that requests three integer values from the user
# and if the three values are unique prints
# ALL UNIQUE
#  otherwise it prints
# DUPLICATES
x, y, z = int(input("#1 ")), int(input("#2 ")), int(input("#3 "))

if x == y or x == z or y == z:
    print("DUPLICATES")
else:
    print("ALL UNIQUE")
