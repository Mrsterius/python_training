def dice(target, faces):

    if target == 0:
        return 1

    acc = 0
    for face in range(1, faces + 1):
        if face > target:
            continue

        acc += dice(target-face, faces)
    return acc

def diceDP(target, faces, memory):

    if target == 0:
        return 1
    if memory.get((target, faces)):
        return memory.get((target, faces))

    acc = 0
    for face in range(1, faces + 1):
        if face > target:
            continue

        acc += diceDP(target-face, faces, memory)
    memory[(target,faces)] = acc
    return acc
print(diceDP(100,5, {}))
