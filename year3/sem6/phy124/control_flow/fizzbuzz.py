for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("fizzbuzz", end="")
    elif num % 3 == 0:
        print("fizz", end="")
    elif num % 5 == 0:
        print("buzz", end="")
    else:
        print(num, end="")

    if num != 100:
        print(", ", end="")

# Answer: fizzbuzz, 91, 92, fizz, 94, buzz, fizz, 97, 98, fizz, buzz
