# Make a function that takes a sequence (like a list, string, or tuple) and a number n and returns
# the last n elements from the given sequence, as a list.
#
# Bonus 1
#
# As a bonus, make your function return an empty list for negative values of n.
#
# Bonus 2
#
# As a second bonus, make sure your function works with any iterable, not just sequences.
#
# See if you can make your function relatively memory efficient (if you're looping over a very long
# iterable, don't store the entire thing in memory).

# TODO Finish test_iterator

def tail(seq, num: int):
    sequence_len = len(list(seq))
    print(f"sequence_len, num: {sequence_len, num}")
    if num <= 0:
        return []
    elif num > sequence_len:
        return list(seq)
    else:
        # print(f"sequence_len: {sequence_len}")
        return list(seq[(sequence_len - num):])

        # self.assertEqual(tail(nums, 2), [9, 16])  # Consuming the generator


if __name__ == '__main__':
    print(tail([1, 2], 1))
    print()

    print(tail([1, 2], 2))
    print()

    print(tail("hello", 0))
    print(tail([1, 2, 3, 4, 5], 0))
    print(tail((6, 7, 8, 9, 0), 0))
    print()

    print(tail("hello", 1))
    print(tail([1, 2, 3, 4, 5], 1))
    print(tail((6, 7, 8, 9, 0), 1))
    print()

    print(tail("hello", 2))
    print(tail([1, 2, 3, 4, 5], 2))
    print(tail((6, 7, 8, 9, 0), 2))
    print()

    print(tail("hello", -2))
    print(tail([1, 2, 3, 4, 5], -2))
    print(tail((6, 7, 8, 9, 0), -2))
    print()

    print(tail("hello", 7))
    print(tail([1, 2, 3, 4, 5], 7))
    print(tail((6, 7, 8, 9, 0), 7))
