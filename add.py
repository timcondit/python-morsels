# https://www.pythonmorsels.com/exercises/cb8fbdd52cf14f8cb31df4f06343cccf/

def add(m1, m2):
    outer = []
    for z1, z2 in zip(m1, m2):
        outer.append([
            iz1 + iz2
            for iz1, iz2 in zip(z1, z2)
            ])
    return outer

# Trey goes even further and adds a second list comprehension. I'm not ready
# for this today. :)
#
# def add(matrix1, matrix2):
#     """Add corresponding numbers in given 2-D matrices."""
#     return [
#         [n + m for n, m in zip(row1, row2)]
#         for row1, row2 in zip(matrix1, matrix2)
#     ]


if __name__ == '__main__':
    matrix1 = [[1, -2], [-3, 4]]
    matrix2 = [[2, -1], [0, -1]]
    print("Expected:\n\t[[3, -3], [-3, 3]]")
    print(f"Got:\n\t{add(matrix1, matrix2)}")

    print()

    matrix3 = [[1, -2, 3], [-4, 5, -6], [7, -8, 9]]
    matrix4 = [[1, 1, 0], [1, -2, 3], [-2, 2, -2]]
    print("Expected:\n\t[[2, -1, 3], [-3, 3, -3], [5, -6, 7]]")
    print(f"Got:\n\t{add(matrix3, matrix4)}")

