def lcs(first, second):
    if len(first) == 0 or len(second) == 0:
        return ""

    if first[0] == second[0]:
        return first[0] + lcs(first[1:], second[1:])
    else:
        left = lcs(first[1:], second)
        right = lcs(first, second[1:])
        if len(left) > len(right):
            return left
        else:
            return right


print(lcs("manan", "amanan"))

def ret_li_lcs(first, second):
    if len(first) == 0 or len(second) == 0:
        return [""]

    if first[0] == second[0]:
        yet = ret_li_lcs(first[1:], second[1:])
        return list(map(lambda item: first[0] + item, yet))
    else:
        left = ret_li_lcs(first[1:], second)
        right = ret_li_lcs(first, second[1:])
        if len(left) > len(right):
            return left
        elif len(left) < len(right):
            return right
        else:
            return left + right

print(ret_li_lcs("manan", "aman"))
