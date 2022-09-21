from random import randrange


def fun1(n):
    result = 0
    while n > 0:
        result += n
        n -= 1
    return result


def fun2(stars):
    for i in range(stars + 1):
        print(end='*')
    print()


def fun3(x, y):
    return 2 * x * x + 3 * y


def fun4(n):
    return 10 <= n <= 20


def fun5(a, b, c):
    return a <= b if b <= c else False


def fun6():
    return randrange(0, 2)


# What gets printed by the following? Or, why is it illegal?
# print("(a)",fun1(5))
# # print("(b)",fun1())
# # print("(c)",fun1(5, 2))
# print('(d)', end=' ')
# print(fun2(5))
# print(fun2(5))
# # e, f, g below
# fun2(5)
# fun2(0)
# fun2(-2)
# print("(h)", fun3(5, 2))
# print("(i)", fun3(5.0, 2.0))
# print("(j)",fun3(A, B))
# print("(k)", fun3(5.0))
# print("(l)",fun3(5.0, 0.5, 1.2))
# print("(m)", fun4(15))
# print("(n)", fun4(5))
# print("(o)", fun4(5000))
# print("(p)", fun5(2, 4, 6))
# print("(q)", fun5(4, 2, 6))
# print("(r)", fun5(2, 2, 6))
# print("(s)",fun5(2, 6))
# print("(t)",fun6())
# print("(u)",fun6(4))
# print("(v)",fun3(fun1(3), 3))
# print("(w)",fun3(3, fun1(3)))
# print("(x)",fun1(fun1(fun1(3))))
print("(y)",fun6(fun6()))
