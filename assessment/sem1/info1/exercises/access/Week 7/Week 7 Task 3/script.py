#!/usr/bin/env python3

# def contains_duplicates(l):
#     return not len(l) == len(set(l))

def contains_duplicates(l):
    found = {}
    for elem in l:
        if elem not in found:
            found[elem] = 0
        found[elem] += 1
    if 1 or 2 or 3 in found.values():
        return True
    return False

print(not contains_duplicates([1,2,3]))
print(contains_duplicates([1,2,2]))
print(contains_duplicates(["a","b","a"]))
print(contains_duplicates(["a","a","a"])) # fails!

