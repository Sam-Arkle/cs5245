# i, j, and k are numbers
# i, j, k, q = 3, 5, 7, 'a' # (a)
# i, j, k, q = 3, 7, 5, 'b' # (b)
# i, j, k, q = 5, 3, 7, 'c' # (c)
# i, j, k, q = 5, 7, 3, 'd' # (d)
# i, j, k, q = 7, 3, 5, 'e' # (e)
i, j, k, q = 7, 5, 3, 'f' # (f)

if i < j:
    if j < k:
        i = j
    else:
        j = k
else:
    if j > k:
        j = i
    else:
        i = k
print(f'q = {q}, i = {i}, j = {j}, k = {k}')