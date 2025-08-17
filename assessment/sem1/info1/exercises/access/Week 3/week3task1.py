#!/usr/bin/env python3

n = 45

# This implementation contains a bug! First, go
# to public/tests.py and implement two more tests.
# Finally, come back here and correct the code
def fizz_buzz():
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return n
print(fizz_buzz())