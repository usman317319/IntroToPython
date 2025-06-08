def add_2_matrix(mat1, mat2):
    for mat in [mat1, mat2]:
        for element in mat:
            if isinstance(element, list):
                pass
            else:
                raise Exception(f"Elements of {mat} must be list.")

    for mat in [mat1, mat2]:
        for element in mat:
            for i in element:
                if isinstance(i, int) or isinstance(i, float):
                    pass
                else:
                    raise Exception(f"{i} has data type {type(i)}, whereas it should be int/float.")
                
    for mat in [mat1, mat2]:
        row_l = len(mat[0])
        for i in mat[1:]:
            if len(i) == row_l:
                pass
            else:
                raise Exception(f"length of each row must be same for a matrix")

    if len(mat1) == len(mat2):
        pass
    else:
        raise Exception(f"Both matrices must have equal number of rows")
    if len(mat1[0]) == len(mat2[0]):
        pass
    else:
        raise Exception(f"Both matrices must have equal number of columns")

    return [[i + j for i,j in zip(mat1[k], mat2[k])] for k in range(len(mat1))]