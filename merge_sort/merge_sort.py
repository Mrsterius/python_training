import sys
n = sys.stdin.read()
arr = [int(x) for x in sys.stdin.read().split()]

def merge(first, second):
    i = 0
    j = 0
    li = []
    while (i < len(first) and j < len(second)):
        if (first[i] < second[j]):
            li.append(first[i])
            i += 1
        else:
            li.append(second[j])
            j += 1
    while (i < len(first)):
        li.append(first[i])
        i += 1
    while (j < len(second)):
        li.append(second[j])
        j += 1
    return li


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    first = arr[:len(arr) // 2]
    second = arr[len(arr) // 2:]
    first = merge_sort(first)
    second = merge_sort(second)
    return merge(first, second)


l = merge_sort(arr)
print(l)