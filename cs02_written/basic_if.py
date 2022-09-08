# 1. Write conditional:
# (a) Write a Python program that prompts the user for an integer value. If the value is among
# the integers from 1 to 100, it prints "OK" otherwise it prints nothing.
user_int = int(input("Please provide an integer between 1 - 100: "))
if 1 <= user_int <= 100:
    print("OK")

# (b) Write a Python program that prompts the user for an integer value. If the value is among
# the integers from 1 to 100, it prints "OK" otherwise it prints "Out of range".
user_int = int(input("Please provide an integer between 1 - 100: "))
if 1 <= user_int <= 100:
    print("OK")
else:
    print("Out of range")
