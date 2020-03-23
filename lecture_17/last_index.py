
def last_index(arr, target, i=0, index=-1):

    if i == len(arr):
        print(index)
        return

    if arr[i] == target:
        index = i

    last_index(arr, target, i+1, index)

last_index([1,2,1,9], 11)
