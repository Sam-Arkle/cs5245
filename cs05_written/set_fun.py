# 23. Given the following initialization statements:
A = {20, 19, 2, 10, 7}
B = {4, 10, 5, 6, 9, 7}
C = {10, 19}
# evaluate the following expressions:
print('(a): ', A)
print('(b): ', 20 in A)
print('(c): ', 20 not in A)
print('(d): ', A & B)
print('(e): ', A | B)
print('(f): ', C < A)
print('(g): ', C <= A)
print('(h): ', C <= B)
print('(i): ', A <= A)
print('(j): ', A < A)
print('(k): ', len(A))
print('(l): ', {x + 2 for x in range(10)})
print('(m): ', {x - 2 for x in A})
print('(n): ', {x - 2 for x in A if x < 10})