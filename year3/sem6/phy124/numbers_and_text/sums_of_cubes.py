for d in range(1, 1001):
    d_cube = d**3
    for a in range(1, d):
        a_cube = a**3
        for b in range(1, a + 1):
            b_cube = b**3
            for c in range(1, b + 1):

                if a_cube + b_cube + c**3 == d_cube:
                    print(a, b, c, d)
                    break


# Possible results: 1 6 8 9, 1 8 6 9, and many more ...
