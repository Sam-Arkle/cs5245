# 3.
# Global
# variables: Consider
# the
# Python
# code
# below and answer
# the
# following:


def sum1(n):
    s = 0
    while n > 0:
        s += 1
        n -= 1
    return s


def sum2():
    global val
    s = 0
    while val > 0:
        s += 1
        val -= 1
    return s


def sum3():
    s = 0
    for i in range(val, 0, -1):
        s += 1
    return s


# def main():


# See each question below for details

# main()  # Call main function
# (a)
# What is printed if main is written as follows?

# def main():
#     global val
#     val = 5
#     print(sum1(val))
#     print(sum2())
#     print(sum3())

# (b) What is printed if main is written as follows?
# def main():
#     val = 5
#     print(sum1(val))
#     print(sum2())
#     print(sum3())

# (c) What is printed if main is written as follows?
# def main():
#     global val
#     val = 5
#     print(sum1(val))
#     print(sum3())
#     print(sum2())

# (d) What is printed if main is written as follows?
# def main():
#     global val
#     val = 5
#     print(sum1(5))
#     print(sum3())
#     print(sum2())

# (e) What is printed if main is written as follows?
# def main():
#     global val
#     val = 5
#     print(sum2())
#     print(sum1(val))
#     print(sum3())

# (f) What is printed if main is written as follows?
# def main():
#     global val
#     val = 5
#     print(sum2())
#     print(sum1(5))
#     print(sum3())




main()