def count_perm(processed, unprocessed):

    if len(unprocessed) == 0:
        return 1

    acc = 0
    for i in range(len(unprocessed)):
        ch = unprocessed[i]
        acc += count_perm(processed + ch, unprocessed[0:i]+unprocessed[i+1:])
    return acc


print(count_perm("", "abcd"))