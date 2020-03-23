def starDown(stars):

    if stars == 0:
        return

    for i in range(stars):
        print("*", end =" ")

    print()

    starDown(stars-1)

    return None

# starDown(5)

def starUp(stars):

    if stars == 0:
        return

    starUp(stars-1)

    for i in range(stars):
        print("*", end =" ")

    print()

# starUp(5)

def starDownRec(row, col = 0):

    if row == 0:
        return
    if row == col:
        print()
        starDownRec(row-1, 0)
        return

    print("*", end=" ")
    starDownRec(row, col + 1)


starDownRec(5)