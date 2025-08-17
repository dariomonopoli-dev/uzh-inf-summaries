#!/usr/bin/env python3

pwd = "aAbB12*-aa"

def is_valid():
    char_low=0
    char_up=0
    digit=0
    special_character=0
    validity=True
    if len(pwd)>=8 and len(pwd)<=16:
        for i in pwd:
            if i.islower():
                char_low+=1
            elif i.isupper():
                char_up+=1
            elif i.isdigit():
                digit+=1
            elif i=="+" or i== "-" or i== "*" or i== "/":
                special_character+=1
            else:
                return False
                break
    if char_low>=2 and char_up>=2 and special_character>=2 and digit>=2:
        validity = True
    else:
        validity=False
    

    # You don't need to change the following line.
    return validity

# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
print(is_valid())

