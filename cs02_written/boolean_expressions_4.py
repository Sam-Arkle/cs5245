# 4. Compound Boolean expressions: Given the following denitions:
x = 3
y = 5
b1 = True
b2 = False
b3 = x == 3
b4 = y < 3
# What expressions are equivalent to the following?
print('(a)', not (b1 and b2 and b3))
print('(b)', not b1 and b2 and b3)
print('(c)', not (b1 and b2 or b3))
print('(d)', not b1 and b2 or b3)
print('(e)', not (b1 or b2 and b3))
print('(f)', not b1 or b2 and b3)
print('(g)', not (b1 or b2 or b3))
print('(h)', not b1 or b2 or b3)
print('(i)', (b1 and b2 and b3))
print('(j)', b1 and b2 and b3)
print('(k)', (b1 and b2 or b3))
print('(l)', b1 and b2 or b3)
print('(m)', (b1 or b2 and b3))
print('(n)', b1 or b2 and b3)
print('(o)', (b1 or b2 or b3))
print('(p)', b1 or b2 or b3)
print('(q)', not (not b1 and not b2 and not b3))
print('(r)', not b1 and not b2 and not b3)
print('(s)', not (not b1 and not b2 or not b3))
print('(t)', not b1 and not b2 or not b3)
print('(u)', not (not b1 or not b2 and not b3))
print('(v)', not b1 or not b2 and not b3)
print('(w)', not (not b1 or not b2 or not b3))
print('(x)', not b1 or not b2 or not b3)