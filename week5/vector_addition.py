import random
def add_2_vectors(vec1, vec2):
    for vec in [vec1, vec2]:
        if isinstance(vec, list):
            pass
        else:
            raise Exception(f"{vec} is of type {type(vec)}. Whereas it must be a list.")

    # for vec in [vec1, vec2]:
    #     for i in vec:
    #         if isinstance(i, int) or isinstance(i, float):
    #             pass
    #         else:
    #             raise Exception(f"The list {vec} contains element {i} which is of type {type(i)}. Whereas it must be either an integer or a floating point value.")

    # if len(vec1) == len(vec2):
    #     pass
    # else:
    #     raise Exception("Length of both Vectors must be same.")

    temp = [None for i in range(len(vec1))]
    for i in range(len(vec1)):
        temp[i] = vec1[i] + vec2[i]
    return temp

v1 = [random.randint(0, 100) for i in range(10000000)]
v2 = [random.randint(0, 100) for i in range(9999999)]
v2.append("3")
add_2_vectors(v1,v2)