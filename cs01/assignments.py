x = 2  # 1
print(f'x = {x:>7.4f}')
y = 3  # 2
b = 2.5  # 3
d = 2 * b  # 4
print(f'd = {d:>7.4f}')
e = 3.5  # 5
print(f'e = {e:>7.4f}')
f = 3 * x  # 6
a = 6  # 7
a += 2  # 8
b -= 2
print(f'b = {b:>7.4f}')  # 9
d = 2 * e  # 10
g = 4 * b - 1
print(f'g = {g:>7.4f}')  # 11
print(f'd = {d:>7.4f}')  # 12
a = b / a
print(f'a = {a:>7.4f}')  # 13
k = 4  # 14
z = k / a
print(f'z = {z:>7.4f}')  # 15
s = 'a'
print('s = {0:>7}'.format(s))  # 16

# ord() returns the number representing the unicode code of a given character
# chr() returns the character for a given unicode code

i = ord(s)
print(f'i = {i:>7.4f}')
w = chr(11)
print(f'w = {w:>7}')  # 17
