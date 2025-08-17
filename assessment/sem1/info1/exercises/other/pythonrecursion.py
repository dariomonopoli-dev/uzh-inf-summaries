def recursive_sum(l):
    sum = 0
    if len(l)==0:
        return sum
    sum+= l[0] + recursive_sum(l[1:])
    return sum
# print(recursive_sum([]))
# print(recursive_sum([1,2]))
# print(recursive_sum([1,2,3,4,5,6]))



def recursive_list_sum(l):
    sum=0
    if not l:
        return 0

    for i in l:
        if isinstance(i, int):
            sum+=i
        if isinstance(i, list):
            sum+=recursive_list_sum(i)
    return sum
# print(recursive_list_sum([]))
# print(recursive_list_sum([1]))
# print(recursive_list_sum([1,2,[3,4,[5,[6,7,[8]]]]]))



def recursive_factorial(n):
    if n == 0 or n == 1:
        return n
    return n * recursive_factorial(n-1)

# print(recursive_factorial(0))
# print(recursive_factorial(1))
# print(recursive_factorial(5))


def fibbo(n):
    if n == 0 or n==1:
        return 1
    return fibbo(n-1) + fibbo(n-2)


assert(fibbo(0) == 1)
assert(fibbo(1) == 1)
assert(fibbo(3) == 3)
assert(fibbo(4) == 5)



def power(x,y):
    if x==0:
        return 0
    if y==0:
        return 1
    return x * power(x, y-1)

print(power(2,1))
print(power(3,4))



def recursive_gcd(a,b):
    if b == 0:
        return  a
    if a == 1:
        return 1
    return recursive_gcd(a, a%b)


print(recursive_gcd(3, 15))



def recursive_sum_of_digits(n):
    if n == 0:
        return 0

    return n%10 + recursive_sum_of_digits(n//10)


print(recursive_sum_of_digits(142))

x = [1, 2, [3, 4, [5, 6]], 7, 8, [9, 10, [11, 12]]]

flattened_list = []

def flatten_list(nested_list):
    if not nested_list:
        return nested_list
    if isinstance(nested_list[0], list):
        return flatten_list(*nested_list[:1]) + flatten_list(nested_list[1:])
    return nested_list[:1] + flatten_list(nested_list[1:])

y = flatten_list(x)
print(sum(y))


y = {"name": {"Valentin": {"Léonard": {"Meyer": "Rosenweg"}}}}

currencies = []

def flatten_dictionary(dictionary):
    for key, value in dictionary.items():
        if  key  not in currencies:
            currencies.append(key)
        if isinstance(value, dict):
            return flatten_dictionary(value)
        currencies.append(value)

flatten_dictionary(y)
print(currencies)

def recursive_upper_reversed_string(s):
    if len(s) == 0:
        return s
    return s[-1:].upper() + recursive_upper_reversed_string(s[:-1])

print(recursive_upper_reversed_string(''))
print(recursive_upper_reversed_string('a'))
print(recursive_upper_reversed_string('reshciw ollah'))






