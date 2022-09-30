def write_n_lines(filename, n):
    with open(filename, 'w') as f:
        for i in range(n):
            f.write(str(i + 1) + '\n')


def sum_lines(filename):
    file_sum = 0
    with open(filename, 'r') as f:
        for line in f:
            file_sum += int(line)

    return file_sum

