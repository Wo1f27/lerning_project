def sum_binary(a, b):
    sum_int = int(a, 2) + int(b, 2)
    res = bin(sum_int)
    return str(res[2:])


print(sum_binary('1100', '1'))