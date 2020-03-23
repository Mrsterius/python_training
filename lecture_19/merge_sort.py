def merge_sort(items):
    if len(items) < 2:
        return items

    first, second = items[:len(items)//2], items[len(items)//2:]

    first, second = merge_sort(first), merge_sort(second)

    return merge(first, second)

def merge(first, second):

    result = []
    i = 0
    j = 0

    while (i < len(first)) and (j < len(second)):
        if first[i] < second[j]:
            result.append(first[i])
            i+=1
        else:
            result.append(second[j])
            j+=1

    while i < len(first):
        result.append(first[i])
        i+=1
    while j < len(second):
        result.append(second[j])
        j+=1

    return result

print(merge_sort([33, 11, 24, 98, 57]))