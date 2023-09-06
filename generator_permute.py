def permute(seq):
    if not seq:
        yield seq
    else:
        for i in range(len(seq)):
            res = seq[:i] + seq[i+1:]
            for x in permute(res):
                yield seq[i:i+1] + x

a = permute([1, 2, 3])
print(list(a))
