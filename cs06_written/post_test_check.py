print('Begin')
try:
    x = int(input())
    print(x)
except ValueError:
    print('Wrong!')
else:
    print('Wow!')
finally:
    print('Done')
print('End')