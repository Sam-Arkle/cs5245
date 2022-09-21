def sum_positive(a):
    sum_ = 0
    for x in a:
        if x > 0:
            sum_ += x
    return sum_


def odds(a):
    return [x for x in a if x % 2 != 0]


print(odds([1, 2, 3, 4]))


def sum_positive_comprehenion(a):
    return sum([x for x in a if x >= 0])


# a = [1, 2, 3, -6]
# print(sum_positive(a))
# print(sum_positive([3, -3, 5, 2, -1, 2]))
# print(sum_positive([-20, 3, -3, 5, 2, -1, 2, 1]))
# print(sum_positive([-20, -3]))
# print(sum_positive([]))

def count_evens(a):
    # even_count = 0

    # for x in a:
    #     if x % 2 == 0:
    #         even_count += 1
    return len([x for x in a if x % 2 == 0])


def count_evens_alt(a):
    even_count = 0

    for x in a:
        if x % 2 == 0:
            even_count += 1
    return even_count

# a = [0, 1, 2, 3, 4, 6, 8]
# print(count_evens(a))
# print(count_evens([3, 5, 4, -1, 2, 0, -8]))
# print(count_evens([3, 5, 4, -1, 0]))
# print(count_evens([3, 5, -1]))
# print(count_evens([]))
