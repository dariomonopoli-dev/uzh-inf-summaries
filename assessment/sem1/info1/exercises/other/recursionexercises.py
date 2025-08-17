# python program counts len of string
def length(s):
    if s == '':return 0
    else: return 1 + length(s[:-1])

print(length('uiasdbhgjbndgnoa')) # prints 11

#python recursive program returns sum of digits of integer

def sumdigits(number):
    # Base Case
    if number == 0:
        return 0
    else:
        # Mod (%) by 10 gives you the rightmost digit (227 % 10 == 7), 
        # while doing integer division by 10 removes the rightmost 
        # digit (227 // 10 is 22)

        return (number % 10) + sumdigits(number // 10)
print(sumdigits(1234))
#fibonacci recursive program
def fib(n):
    if n==0 or n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)
print(fib(5))