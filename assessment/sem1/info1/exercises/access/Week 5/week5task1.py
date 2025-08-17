#!/usr/bin/env python3

# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!

def merge(a, b):
        mergelist = []
        if len(a) == 0 or len(b) == 0:
            return mergelist
        if len(a) > len(b):
            for i in range(len(b)):
                mergelist.append((a[i], b[i]))
            for i in range(len(a) - len(b)):
                mergelist.append((a[i+len(b)-len(a)], b[len(b) - 1]))
        elif len(a) < len(b):
            for i in range(len(a)):
                mergelist.append((a[i], b[i]))
            for i in range(len(b) - len(a)):
                mergelist.append((a[len(a)-1], b[i+len(a)-len(b)]))
        else:
            mergelist = [(a[j], b[j]) for j in range(len(a))]
        return mergelist



# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!
print(merge([2,1,0], [5, 6]))
