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

    new_lst = []

    # for a pair of lists
    for i in range(len(lol1)):
        for j in range(len(lol2)):
            new_lst.append([lol1[i][j] + lol2[i][j]])
    return new_lst

    
if __name__ == '__main__':
#    lst1 = [1, -2]
#    lst2 = [2, -1]
#    x = add(lst1, lst2)
#    print(x)

    matrix1 = [[1, -2], [-3, 4]]
    matrix2 = [[2, -1], [0, -1]]
    print(add(matrix1, matrix2))
