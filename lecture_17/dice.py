def dice(processed, target, faces):

    if target == 0:
        print(processed)
        return

    for face in range(1, faces + 1):
        if face > target:
            continue

        dice(processed + str(face), target - face, faces)

# dice("", 5, 3)

def count_dice(processed, target, faces):

    if target == 0:
        if len(processed) <= 3:
            return 1
        else:
            return 0

    acc = 0
    for face in range(1, faces + 1):
        if face > target:
            continue

        acc += count_dice(processed + str(face), target - face, faces)

    return acc

# print(count_dice("",5,3))

def ret_dice(processed, target, faces):

    if target == 0:
        return [processed]
    acc = []
    for face in range(1, faces + 1):
        if face > target:
            continue

        acc.extend(ret_dice(processed + str(face), target - face, faces))

    return acc

print(ret_dice("",5,3))