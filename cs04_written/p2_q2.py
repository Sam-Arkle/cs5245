# 2. Legal or Illegal 3:
# (a) What does the following do and why?
def proc(x):
    num = 2 * x * x


def main():
    num = 10
    proc(num)
    print(num)


main()


# (b) What does the following do and why?
# def proc(x):
#     return 2 * x * x
# def main():
#     x = 10
#     print(proc(num))
# main()

# (c) What does the following do and why?
def proc(x):
    return 2 * x * x


def main():
    y = 10
    print(proc(y))


main()
