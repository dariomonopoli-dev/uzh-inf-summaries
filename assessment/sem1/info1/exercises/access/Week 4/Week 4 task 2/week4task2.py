#!/usr/bin/env python3

import os
def test(x):
    try:
        float(x)
        return True
    except ValueError:
        return False


# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!
def get_average_grade(path):
    list=[]
    if not os.path.exists(path):
            return None
    else:
            with open(path, 'r') as f:
                lines=f.readlines()
            for line in lines:
                semicolon=line.find(':')
                if ':' in line and test(line[semicolon+1:]):
                    list.append(float(line[semicolon+1:]))
            if len(list)==0:
                return 0.0
            elif len(list)!=0:
                formula=(sum(list[:]))/len(list)
                return formula


# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!
print(get_average_grade("public/my_grades.txt"))

