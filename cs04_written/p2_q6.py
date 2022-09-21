# 6. Programming GCD:
# (a) Rewrite the gcd function shown below so that it implements Euclid's method (i.e., not
# the one in the textbook) but uses iteration instead of recursion.
def gcd_recursive(m, n):
    if n == 0:
        return m
    else:
        return gcd_recursive(n, m % n)


def gcd_iterative(m, n):
    gcd = 0
    bigger_int = 0
    smaller_int = 0
    if m == n:
        return m
    elif m > n:
        bigger_int = m
        smaller_int = n
    else:
        smaller_int = m
        bigger_int = n

    for x in range(smaller_int, 0, -1):
        if bigger_int % x == 0 and smaller_int % x == 0:
            gcd = x
            break

    return gcd
