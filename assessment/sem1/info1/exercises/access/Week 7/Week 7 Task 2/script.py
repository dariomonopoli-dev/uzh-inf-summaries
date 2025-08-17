#!/usr/bin/env python3

def where_is_waldo(names):
    if "Waldo" in names:
        return names.index("Waldo")
    return None

print(where_is_waldo(["Peter", "Waldo", "John"]) == 1)
print(where_is_waldo(["Peter", "Willy", "John"]) == None)
print(where_is_waldo([]) == None)

