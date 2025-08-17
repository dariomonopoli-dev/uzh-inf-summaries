#!/usr/bin/env python3

# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!
def is_prime(n):
    if isinstance(n, int) and n >0:
        if n==1:
            return f'{n} is the multiplicative identity'
        
        if n>1:
                for i in range(2,n+1):
                    if n==i:
                        return f'{n} is prime'   
                    elif n%i==0: 
                        return f'{n} is not a prime number ({i} * {n//i} = {n})'
        
                    

# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!
print(is_prime(15))