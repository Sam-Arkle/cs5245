# (a) Write a basic Python program (no imports or data structures like lists) that uses the
# appropriate loop to prompt the user to enter 10
# oating-point values. Then, program
# prints the sum, average (mean), maximum, and minimum of the values, in that order.
# y = float(input("Please give a float: "))
# sum_y = y
# maximum = y
# minimum = y
# for x in range(1, 10):
#     y = float(input("Please give another float: "))
#     sum_y += y
#     if y > maximum:
#         maximum = y
#     if y < minimum:
#         minimum = y
# average_y = sum_y / 10
# print(f'Sum = {sum_y}, average = {average_y}, maximum = {maximum}, minimum = {minimum}')

# (b) Write a basic Python program (no imports or data structures like lists) that uses the
# appropriate loop to prompt the user to enter any number of nonnegative
# oating-point
# values. The user terminates the input by entering a negative value. Then, program
# prints the sum, average (mean), maximum, and minimum of the values, in that order.
# The terminating negative value is not used in the computations.

y = float(input("Please give a positive float: "))
sum_y = y
maximum = y
minimum = y
number_of_numbers = 1
while y >= 0:
    y = float(input("Please give another positive float: "))
    if y < 0:
        average_y = sum_y / number_of_numbers
        print(f'Sum = {sum_y}, average = {average_y}, maximum = {maximum}, minimum = {minimum}')
        break
    sum_y += y
    number_of_numbers += 1
    if y > maximum:
        maximum = y
    if y < minimum:
        minimum = y


else:
    print(f'{y} is negative. Try a positive number next time!')

# print(f'Sum = {sum_y}, average = {average_y}, maximum = {maximum}, minimum = {minimum}')
# Code not working as intended if negative given initially!
