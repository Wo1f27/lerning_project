def addTwoNumbers(l1, l2):
    str_l1, str_l2 = [str(i) for i in l1], [str(i) for i in l2]
    rev_l1, rev_l2 = str_l1[::-1], str_l2[::-1]
    summ_l1_l2 = int(''.join(rev_l1)) + int(''.join(rev_l2))
    res = [x for x in str(summ_l1_l2)]
    res = res[::-1]
    return res

print(addTwoNumbers([1, 2, 4], [3, 2, 3]))