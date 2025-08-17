import numpy as np


def filter(seq, ignore):
    l = []
    for el in seq:
        if el not in ignore:
            l.append(el)

    print(l)
    return l


def find(seq, val):
    l = []
    for i, el in enumerate(seq):
        if el == val:
            l.append(i)
    print(l)
    return l


def common(seq1, seq2):
    l = []
    for el in seq1:
        if el in seq2 and el not in l:
            l.append(el)
    print(l)
    return l


def find_largest(l1, l2):
    largest = max(filter(common(l1, l2), [" ", None]))
    print(int(find(l1, largest)[0]), int(find(l2, largest)[0]))


l1 = [
    79,
    92,
    41,
    32,
    " ",
    35,
    40,
    36,
    13,
    43,
    " ",
    " ",
    20,
    77,
    28,
    67,
    62,
    45,
    95,
    51,
    38,
    31,
    46,
]
l2 = [
    " ",
    97,
    20,
    33,
    29,
    " ",
    " ",
    23,
    76,
    21,
    22,
    85,
    49,
    14,
    44,
    99,
    59,
    19,
    13,
    90,
    87,
    28,
    72,
]

find_largest(l1, l2)
