
import random
from typing import AsyncGenerator

# These variables are required for the automatic grading to work, do not change
# their names. You can change values of these variables.
min_length_global = 0
max_length_global = 5
char_start_global = 30
char_end_global = 65


# This signature is required for the automated grading to work.
# You must not rename the function or change its list of parameters.
def fuzzer(min_length, max_length, char_start, char_end):
    string_length=random.randrange(min_length,max_length+1)
    out=''
    for i in range(string_length):
        out+=chr(random.randrange(char_start, char_end+1))
    return out



# This signature is required for the automated grading to work.
# You must not rename the function or change its list of parameters.
def calculate_factorial(inp):
    if inp==None:
        return None
    else:
        try:
            int(inp)
        except:
                raise TypeError("TypeError: string")
        else:
            number=int(inp)
        if number<0:
            raise ValueError("ValueError: number negative")
        if number>10:
            raise ValueError("ValueError: number too large")  
        else:
            fact = 1
            for num in range(1, number + 1):
                fact *= num
            return fact

                


def run(trials):
    myList = []
    for i in range(trials):
        calculator_input=fuzzer(min_length_global, max_length_global, char_start_global, char_end_global)
        try:
            calculate_factorial(calculator_input)
            
        except ValueError as error_message:
            returned_tuple = (1, str(error_message))
        except:
            returned_tuple = (1, 'Other error')
        else:
            returned_tuple=(0,'')
        myList.append(returned_tuple)
    return myList



print(run(1))


class MyClass:
    def __init__(faccio,age, breed):
      faccio.age = age
      faccio.breed = breed
    def function(faccio):
        return faccio.age
d1= MyClass(2,'ciao')

print(d1.function())