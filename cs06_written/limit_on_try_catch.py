try:
    pass
finally:
    pass


# 12. For the next set of questions show what each program will print when the user supplies the indicated
# input text.
# Write *EXCEPTION* if and when the execution will generate an exception stack trace for an un-
# caught exception.
# (a)
print('Begin')
x = int(input())
print(x)
print('End')

# i. User enters 22
# 	>>>22
# 	>>>End
# ii. User enters ZZ
# 	>>>EXCEPTION
# 	>>>
# (b)
print('Begin')
try:
    x = int(input())
    print(x)
except ValueError:
    print('Wrong!')
print('End')
# i. User enters 22
# 	>>> 22
# 	>>> End
# ii. User enters ZZ
# 	>>> Wrong!
# 	>>> End
# (c)
print('Begin')
try:
    x = int(input())
    print(x)
except IndexError:
    print('Wrong!')
print('End')
# i. User enters 22
# 	>>>22
# 	>>>End
# ii. User enters ZZ
#     >>>EXCEPTION
# (d)
print('Begin')
try:
    x = int(input())
    print(x)
except Exception:
    print('Wrong!')
print('End')
# i. User enters 22
#     >>> 22
# 	>>> End
# ii. User enters ZZ
#     >>>Wrong!
# 	>>>End
# (e)
print('Begin')
try:
    x = int(input())
    print(x)
except ValueError:
    print('Wrong!')
else:
    print('Wow')
print('End')
# i. User enters 22
#     >>>Begin
# 	>>>22
# 	>>>Wow
# 	>>>End
# ii. User enters ZZ
#     >>>Begin
# 	>>>Wrong!
# 	>>>End
# (f)
print('Begin')
try:
    x = int(input())
    print(x)
except ValueError:
    print('Wrong!')
finally:
    print('Done')
print('End')
# i. User enters 22
#     >>>Begin
#     >>>22
#     >>>Done
#     >>>End
# ii. User enters ZZ
# 	>>>Begin
#     >>>Wrong!
#     >>>Done
#     >>>End

# (g)
print('Begin')
try:
    x = int(input())
    print(x)
except ValueError:
    print('Wrong!')
else:
    print('Wow')
finally:
    print('Done')
print('End')
# i. User enters 22
#     >>>Begin
# 	>>>22
# 	>>>Wow
# 	>>>Done
# 	>>>End
# ii. User enters ZZ
#     >>>Begin
# 	>>>Wrong!
# 	>>>Done
# 	>>>End