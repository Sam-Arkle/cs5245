# we were asked to simplify x < 0 or x > 1
#My answer was: x != (0 and 1). Is this valid syntax?

x = int(input("Test it: "))
if x != (0 and 1):
    print("Happy days")
else:
    print("You lost a mark")

# This doesn't work as it evaluates to: x =! 0 or x =! 1 which will be true in all cases...
