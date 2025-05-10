def add(vec1, vec2):
    if len(vec1) == len(vec2):
        pass
    else:
        print("Error")

    for i in [vec1, vec2]:
        if isinstance(i, list):
            pass
        else:
            print("Error")     # Replace with Error Exception

    for vec in [vec1, vec2]:
        for i in vec:
            if isinstance(i, int) or isinstance(i, float):
                pass
            else:
                print("Error")

    temp = [None for i in range(len(vec0))]

    for i in range(len(vec1)):
        temp[i] = vec1[i] + vec2[i]

    return temp

print(add([3, 4], [2, 3]))
