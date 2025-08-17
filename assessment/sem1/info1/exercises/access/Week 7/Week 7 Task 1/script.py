#!/usr/bin/env python3

def invert_casing(text):
    res = ""
    for c in text:
        if c.isupper():
            res += c.lower()
        else:
            res += c.upper()
    return res

