# 2. Creating lists: Express the list created by each of the following.
# print("(a)", [8] * 4)
# print("(b)", 6 * [2, 7])
# print("(c)", [1, 2, 3] + ['a', 'b', 'c', 'd'])
# print("(d)", 3 * [1, 2] + [4, 2])
# print("(e)", 3 * ([1, 2] + [4, 2]))

# 3. Evaluating list comprehensions: What list is created by the following?
# print("(a)",  [x + 1 for x in [2, 4, 6, 8]])
# print("(b)",  [10 * x for x in range(5, 10)])
# print("(c)",  [x for x in range(10, 21) if x % 3 == 0])
# print("(d)",  [(x, y) for x in range(3) for y in range(4)])
# print("(e)",  [(x, y) for x in range(3) for y in range(4) if (x + y) % 2 == 0])

# 4. Writing list comprehensions: What list comprehension generates the following?
print("(a)", [1, 4, 9, 16, 25])
print([x ** 2 for x in range(1, 6)])
print("(b)", [0.25, 0.5, 0.75, 1.0, 1.25, 1.5])
print([x / 4 for x in range(1, 7)])
print("(c)", [('a', 0), ('a', 1), ('a', 2), ('b', 0), ('b', 1), ('b', 2)])
print([(x, y) for x in ['a', 'b'] for y in range(3)])
