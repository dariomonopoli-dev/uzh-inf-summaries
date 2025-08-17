#!/usr/bin/env python3

s = "aB:cD"

# perform the transformation
def transform_string():
    pos=s.find(':')
    string_before=s[0:pos]
    string_after=s[pos:]
    formula1=string_before.lower()
    formula2=string_after.upper()
    # Insert your code here.
    # You may want to use several variables to
    # store temporary values (such as the index of
    # the colon or the two strings before and after
    # it). Then, you can construct the final result
    # from your temporary variables.
    res = formula1+formula2

    # You don't need to change the following line.
    # It simply returns the string created above.
    return res
print(transform_string())