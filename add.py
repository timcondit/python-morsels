# https://www.pythonmorsels.com/exercises/cb8fbdd52cf14f8cb31df4f06343cccf/

def add(lol1, lol2):
    """Accepts two lists-of-lists of numbers and returns one list-of-lists with
    each of the corresponding numbers in the two given lists-of-lists added
    together.

    It should work something like this:

    >>> matrix1 = [[1, -2], [-3, 4]]
    >>> matrix2 = [[2, -1], [0, -1]]
    >>> add(matrix1, matrix2)
    [[3, -3], [-3, 3]]
    >>> matrix1 = [[1, -2, 3], [-4, 5, -6], [7, -8, 9]]
    >>> matrix2 = [[1, 1, 0], [1, -2, 3], [-2, 2, -2]]
    >>> add(matrix1, matrix2)
    [[2, -1, 3], [-3, 3, -3], [5, -6, 7]]
    """

    # handles variable number of lists
    outer = []
    for first, second in zip(lol1, lol2):
        inner = []
        for fst, scd in zip(first, second):
            inner.append(fst + scd)
        outer.append(inner)
    return outer

    
if __name__ == '__main__':
    matrix1 = [[1, -2], [-3, 4]]
    matrix2 = [[2, -1], [0, -1]]
    print("Expected:\n\t[[3, -3], [-3, 3]]")
    print(f"Got:\n\t{add(matrix1, matrix2)}")

    print()

    matrix1 = [[1, -2, 3], [-4, 5, -6], [7, -8, 9]]
    matrix2 = [[1, 1, 0], [1, -2, 3], [-2, 2, -2]]
    print("Expected:\n\t[[2, -1, 3], [-3, 3, -3], [5, -6, 7]]")
    print(f"Got:\n\t{add(matrix1, matrix2)}")

