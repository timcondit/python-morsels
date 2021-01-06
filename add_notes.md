# add.py notes

## https://www.pythonmorsels.com/exercises/cb8fbdd52cf14f8cb31df4f06343cccf/

* zip() behaves sort of like a transpose. It unpacks lists, and swaps
  "horizontal" for "vertical".

* Effect on two-list (square: 2x2) matrices. Converts

```
[[1, 2], [3, 4]] -> [1, 2] [5, 6]
[[5, 6], [7, 8]]    [3, 4] [7, 8]
```

* Effect on three-list (rectangular: 3x2) matrices shows unpacking and
pairing more clearly.

```
[[1, 2], [3, 4],  [5, 6]]   -> [1, 2] [7, 8]
[[7, 8], [9, 10], [11, 12]]    [3, 4] [9, 10]
                               [5, 6] [11, 12]
```


* Another transform. Unpacks lists, and swaps horizontal for vertical.

```
[1, -2] [2, -1]
1 2
-2 -1

[-3, 4] [0, -1]
-3 0
4 -1
```

* With three-list matrices. First transform. From this:

```
[[1, -2, 3], [-4, 5, -6], [7, -8, 9]]
[[1, 1, 0], [1, -2, 3], [-2, 2, -2]]
```

To this:

```
[1, -2, 3] [1, 1, 0]
[-4, 5, -6] [1, -2, 3]
[7, -8, 9] [-2, 2, -2]
```

And then to this, with spaces added:

```
1 1
-2 1
3 0

-4 1
5 -2
-6 3

7 -2
-8 2
9 -2
```

