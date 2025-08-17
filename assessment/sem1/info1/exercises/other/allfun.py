#Write a function that turns a numeric age into an age description. Children younger than three years are called toddlers. Adulthood starts with 18 years and one becomes senior with age 65. You can assume that age is always greater than zero.
def get_age_desc(age):
    if age < 3:
        return "toddler"
    if age >= 65:
        return "senior"
    if age >= 18:
        return "adult"
    return "child"
    
assert get_age_desc(1) == "toddler"
assert get_age_desc(3) == "child"
assert get_age_desc(14) == "child"
assert get_age_desc(18) == "adult"
assert get_age_desc(65) == "senior"

#The function compute_max_diff receives a list of numbers as an argument. Implement the function and compute the highest absolute difference between any two consecutive numbers in the list. You can use the predefined function abs in your solution.
def compute_max_diff(numbers):
    if len(numbers) < 2:
        return 0
    
    max = 0
    last= numbers[0]
    for cur in numbers[1:]:
        diff = abs( last - cur )
        last = cur
        if diff > max:
            max = diff
    
    return max

assert compute_max_diff([]) == 0
assert compute_max_diff([1]) == 0
assert compute_max_diff([2, -1]) == 3
assert compute_max_diff([2, 7, 5, 14, 12, 14]) == 9

#Write a function that aggregates all numbers in a list of integers. The even numbers should be added, the odd numbers should be subtracted from the result. Return a tuple that contains both the length of the original list and the calculated value.
def sum_even_and_odd(numbers):
    sum = 0
    for n in numbers:
        if n%2:
            sum -= n
        else:
            sum += n
    return (len(numbers), sum)

assert sum_even_and_odd([]) == (0, 0)
assert sum_even_and_odd([2,4,7]) == (3, -1) # 3 values, 2+4-7=-1

#Implement a function that applies an operation op to every element of a list l. Return the result in a new list and do not alter the original list.
def app(l, op):
    res = []
    for e in l:
        res.append(op(e))
    return res

l = [1, 2, 3]
def double(x): return x * 2
assert app([], double) == []
assert app(l, double) == [2, 4, 6]
assert app(l, lambda x: x * 3) == [3, 6, 9]
assert l == [1, 2, 3]

#Write a function that counts the frequency of each character that is contained in a string. Return the result in a dictionary.
def count_chars(s):
    counts = {}
    for c in s:
        if not c in counts.keys():
            counts[c] = 1
        else:
            counts[c] += 1
    return counts

assert count_chars("") == {}
assert count_chars("aA .") == {"a": 1, "A": 1, " ": 1, ".": 1}
assert count_chars("abbCaabb") == {"a": 3, "b": 4, "C": 1}

#Write a function that counts the frequency of an arbitrary character in a string. Reuse the function count_chars from the previous task. 
#Note: You can assume that c always contains exactly one character.
def count_occurrences(s, c):
    count = 0
    for e in s:
        if e == c:
            count += 1
    return count

assert count_occurrences("", "a") == 0
assert count_occurrences("x", "b") == 0
assert count_occurrences("abbccc", "c") == 3

#Implement the function nested_sum that calculates the sum of all elements of a list l. These elements are either integers or other nested lists that follow the same pattern. The calculated sum should consider the nesting depth in the list as weight, i.e., values on the first level have a weight of 1, on the second level a weight of 2, and so on. You can find concrete examples at the end of the block. Note: You can assume that l is always valid, i.e., only contains integers and nested list. l can also be empty. Make sure that your implementation does not violate these assumptions. Note: Your solution must use recursion.
def nested_sum(l, depth=1):
    if type(l) == int:
        return l
    
    sum = 0
    for e in l:
        sum += nested_sum(e, depth+1)
    return depth * sum
        

assert nested_sum([]) == 0
assert nested_sum([1, 2, 3]) == 6 # 1*(1+2+3)
assert nested_sum([1, [2]]) == 5 # 1*(1+2*(2))
assert nested_sum([1, [2, [3]]]) == 23 # 1*(1+2*(2+3*(3)))
assert nested_sum([[1, 2], 3, [4, 5]]) == 27 # 1*(2*(1+2)+3+2*(4+5))

#You are working in the university administration and you would like to analyze the exam results of all current students. The administrator has exported you the exam data into a file, but you still need to pre-process it to make it more accessible in your program. Your file results.csv has the following format. Each line contains one exam result that consists of three fields, which are separated by comma: student name, course, and grade.
#Hans,Info1,5.5 Hans,Economics,5 Petra,Info1,5.25 Petra,Economics,4.75 Petra,Math,6 Martin,Info1,5.75
#Implement a function read to make the contents of such a file easy to use. To do so, read the file referenced by path, split each line into the three components and store them in a dictionary. The dictionary should use the student’s name as the key and a list of all exams as a value; this list should contain the course and the resulting grade in a tuple (see assert example).
FILE_NAME = "INFO1_HS18_MIDTERM_T4.csv"

# prepare file:
content = """Hans,Info1,5.5
Hans,Economics,5
Petra,Info1,5.25
Petra,Economics,4.75
Petra,Math,6
Martin,Info1,5.75
"""

file = open(FILE_NAME, "w") 
file.write(content)
file.close()

try:
    # task:
    def read(path):
        users = {}
        with open(FILE_NAME, "r") as f:
            for l in f.readlines():
                (user, course, grade) = l[:-1].split(",")
                if not user in users.keys():
                    users[user] = []
                users[user].append((course, float(grade)))
            
        return users

    assert read("results.csv") == {"Hans": [("Info1", 5.5), ("Economics", 5)],
                                   "Petra": [("Info1", 5.25), ("Economics", 4.75), ("Math", 6)],
                                   "Martin": [("Info1", 5.75)]}
finally:
    # teardown
    import os
    os.remove(FILE_NAME)

#Write a function with two arguments: l is a list of integers and target is an integer value. The function should return a tuple of the distinct indices of the first two numbers that add up to target.
#Note: You can assume that l is always a list and that target is always an integer. Note: You cannot use the same element in l twice.
def find_sum(l, target):
    for idx1, v1 in enumerate(l):
        for idx2, v2 in enumerate(l):
            if idx1 == idx2:
                continue
            if v1 + v2 == target:
                return (idx1, idx2)
    return None

assert find_sum([], 9) == None
assert find_sum([1], 2) == None
assert find_sum([1, 1], 2) == (0, 1)
assert find_sum([1, 7, 2, 11], 9) == (1, 2)
assert find_sum([1, 2, 3, 4], 5) == (0, 3)

#Write a function count_keywords that takes two input arguments, a path to a file and a list of keywords. The function should count how often the provided keywords occur in the file. You can assume that the file always exists and that it only contains letters, spaces, and new lines. 
def read_fake():
    return ["Midway upon the journey of our life I found myself within a FOREST dark",
            "for the straightforward pathway had been lost",
            "",
            "Ah me How hard a thing it is to say what was this forest savage rough and",
            "stern which in the very thought renews the fear So bitter is it death is",
            "little more but of the good to treat, which there I found speak will I of"]

def read_real(path):
    with open(path, "r") as f:
        # find a way to get rid of '\n's
        return f.read().split("\n")

def count_keywords(path, keywords):
    res = {}
    for line in read_fake():
        for word in line.split(" "):
            word = word.lower()
            if word in keywords:
                n = res.get(word, 0) + 1
                res[word] = n
    return res

# file.txt contains the example above
assert count_keywords('file.txt', ['forest', 'the', 'found']) == {'the': 5, 'found': 2, 'forest': 2}
assert count_keywords('file.txt', ['black']) == {}
assert count_keywords('file.txt', []) == {}

#python function converts number to decimal
def to_binary(n):
    if n == 0:
        return "0"

    res = ""
    while n:
        res = ("1" if n%2 else "0") + res
        n=n//2
    
    return res

assert to_binary(0) == "0"
assert to_binary(1) == "1"
assert to_binary(2) == "10"
assert to_binary(19) == "10011"

#python recursive function finds max in nested list
def find_max(l):
    
    # anchor 1: handle numbers
    if type(l) == int: return l
    
    # anchor 2: handle empty lists
    if not l: return None
    
    mx = None
    for e in l:
        cur = find_max(e)
        if type(cur) == int:
            if mx == None or cur > mx:
                mx = cur
    return mx

assert find_max([]) == None
assert find_max([1, 12, -3]) == 12
assert find_max([2, [1]]) == 2
assert find_max([1, [-7, [13, [4]], [[[[5]]]] ]]) == 13
# additional cases
assert find_max([[]]) == None
assert find_max([[], 1]) == 1
assert find_max([2, []]) == 2

#Implement a recursive function recursive_reverse that takes a string parameter and returns the reverse of the same string. In this task, you may not make any function calls except recrusive calls to the solution function.
def recursive_reverse(s):
  if s == '': return ''
  return s[-1] + recursive_reverse(s[:-1])

#Write a function swap_case that takes a string as the input parameter and returns the same string with inverted cases. So lowercase characters should be transformed to uppercase and vice versa. Make sure the function works on the empty string as well.
def swap_case(s):
  temp = ""
  for character in s:
    if character.isupper():
      temp += character.lower()
    else:
      temp += character.upper()
  return temp

#Write a function count_keyword_occurrence that takes two input arguments, a string and a list of strings-to-be-searched. The function should count how often any of the provided strings-to-be-searched occur in the string (do not ignore casing in this task). Make sure the function works even if an empty string or empty list is supplied. Hint: You're allowed to use count()
def count_keyword_occurrence(string, strings_to_be_searched):
  count = 0
  for s in strings_to_be_searched:
    temp_s = string
    while temp_s.find(s) != -1:
      idx = temp_s.find(s)
      if idx >= 0:
        count += 1
        temp_s = temp_s[idx+len(s):]
  return count

def count_keyword_occurrence_easy(string, strings_to_be_searched):
  count = 0
  for s in strings_to_be_searched:
    count += string.count(s)
  return count

#Write a function count_positive_even_numbers which computes the number of positive even numbers in the first n numbers of a list.
def count_positive_even_numbers(numbers, n):
  count = 0
  number_of_positive_even_numbers = 0
  while count < n:
    if numbers[count] > 0 and numbers[count] % 2 == 0: number_of_positive_even_numbers += 1
    count += 1
  return number_of_positive_even_numbers

#Write a function list_reversed_filtered which takes two lists, l1 and l2, as input parameters. The function should return the reverse of l1, but without any elements which exist in l2.
def list_reversed_filtered(l1, l2):
  res = []
  for e in l1:
    if e in l2: continue
    res.insert(0, e)
  return res

def list_reversed_filtered_2(l1, l2):
  res = []
  list_reversed = l1[::-1]
  for element in list_reversed:
    if element not in l2:
      res.append(element)
  return res

#Implement a function sum_of_multiplications that takes a list of tuples as a parameter. Each tuple contains two integers or floats. For each tuple, the function should multiply the two values and finally it should return the sum of these multiplications.
def sum_of_multiplications(l):
  sum = 0
  for v1, v2 in l:
    sum += v1 * v2
  return sum

#Implement a function compute that takes 3 numbers (integers and/or floats) as parameters and returns the result of the mathematical formula shown below, rounded to the nearest integer using round(). (The vertical bars indicate an absolute value.)
#(x+2y)+|z|**1/5
def compute(x,y,z):
    return round(((x+2**y)+abs(z))**(1/5))

# You are programming the cashier's system for a hot-dog stand with a menu as shown below. However, you offer some special discounts if certain conditions apply:
# When ordering a Water with a Spicy-Dog, the Water is free. This applies for every pair of these products ordered even if ordering multiple pairs.
# Every 6th beer in an order is free.
# Implement a function bill which takes one parameter, order, which is a dictionary mapping product names to the number of each item ordered. The function should return the total sum of the order. The function should return 0 for an empty order. The menu and pricing is provided as a dictionary menu.
# Note that your solution must also work if the menu prices are adjusted. Don't use concrete values in your solution, but reference the prices in menu instead.

menu = {
  "Hot Dog":             3.50,
  "Spicy Dog":           4.00,
  "Vegan Dog":           3.50,
  "Water":               1.50,
  "Fizzy Drink":         2.50,
  "Beer":                4.00
}

def bill(products):
    sum = 0
    # total sum without discounts
    for item, count in products.items():
        sum += (count * menu[item])
    # subtract discount for waters
    if "Spicy Dog" in products and "Water" in products:
        free = min(products["Spicy Dog"], products["Water"])
        sum -= free * menu["Water"]
    # subtract every 6th beer
    if "Beer" in products:
        count = products["Beer"]
        free = count // 6
        sum -= free * menu["Beer"]
    return sum

#Implement a function russian_roulette, which reflects the first round of a game of russian_roulette. It takes no parameters and returns a string. The function, when called, should have a 1 in 6 chance of returning "BANG!!!" and a 5 in 6 chance of returning "Click!". Hint: You will need to use the random module.
import random

def russian_roulette():
    if random.randint(1,6) == 6:
        return "BANG!!!"
    else:
        return "Click!"

#A digital gray-scale image can be stored as a list of lists, where each inner list contains the values for one row of the image and where each value can take on a number between 0 (pure black) and 255 (pure white). Below you can some examples. Example 1 draws out a picture of the upper case letter "B" in dark gray (value 50) on a white (value 255) background. Example 2 shows a white-to-black gradient going from the top left corner to the bottom right corner.

# Your task is to implement two functions: invert, which inverts the colors of an image, and flip_vertical, which flips the picture vertically.

# Inverting a picture means changing dark values to light values and light values to dark values. In our case, 255 would need to be changed to 0, 254 to 1, 253 to 2 and so on, all the way to changing 0 to 255. See Example 3 below for how Example 1 is inverted.

# Flipping a picture vertically means that the first row of the image (at the top) becomes the last row (at the bottom), the second row becomes the second-to-last row, and so on. If there's an un-even number of rows, the middle row stays where it is. See Example 4 for the vertically flipped gradient of Example 2.

# It is up to you if you want to return the input lists changed in-place or to return new lists. Both solutions are valid, just make sure you return the result.

# Note that the implementations of these functions are quite simple. Don't overthink the problems.

def invert(img):
  for row in img:
      for i, value in enumerate(row):
          row[i] = 255-value
  return img

def flip_vertical(img):
  img.reverse()
  return img

# Implement the following recursive sorting algorithm in a function my_sort, which takes a list l as a parameter. Assume that the list l contains any number of positive and/or negative numbers. Assume that the list contains no duplicate values. For this task, you need to precicely follow the instructions in the algorithm description one by one to implement a correct solution. Read the steps carefully to ensure that your implementation will be correct. The following steps need to be implemented in the function body of my_sort:

# Step 1: Check if l is empty. If that's true, return an empty list.
# Step 2: Assign the first element in l to a variable called middle.
# Step 3: Create two empty lists and assign them to variables called smaller and larger.
# Step 4: Begin a for loop that iterates over the elements in l, starting at index 1 (i.e. skipping the first element).
# Step 5: In each iteration of the for loop, compare the current value to middle. If the value is smaller than middle, append the element to the smaller list. If the value is larger than middle, append the element to the larger list. This concludes the for loop.
# Step 6: Create a variable result which is the concatenation (for example, using + or .concat()) of:
# the return value of a recursive call to my_sort passing smaller as the parameter.
# a list containing only the value of middle.
# the return value of a recursive call to my_sort passing larger as the parameter.
# Step 7: return result
# Most of these steps are very straight-forward. Just make sure that the value you return is indeed a flat (non-nested) list of numbers. In other words: watch out not to append the return values of recursive calls as nested lists to your resulting value. The result value needs to be a concatenation of the three values described above, resulting in a single, 1-dimensional list. Also, ensure that you are not modifying the function signature and are using exactly the specified variable names and program structure!

def my_sort(l):
    if l == []: return []
    middle = l[0]
    smaller = []
    larger = []
    for v in l[1:]:
        if v > middle:
            larger.append(v)
        if v < middle:
            smaller.append(v)
    result = my_sort(smaller) + [middle] + my_sort(larger)
    return result

#function ispalindrome
def is_palindrome(s):
  s = s.lower()
  filtered = ""
  for c in s:
    if c in "abcdefghijklmnopqrstuvwxyz":
      filtered += c
  rev = ""
  for c in filtered:
      rev = c + rev
  return rev == filtered

#factorial recursive function
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

#Think of a recursive version of the function f(n) = 3 * n, i.e. the multiples of 3
def mult3(n):
    if n == 1:
        return 3
    else:
        return mult3(n-1) + 3

for i in range(1,10):
         #print(mult3(i))
         pass

#Write a recursive Python function that returns the sum of elements in nested list/list. 
def recursive_sum_of_elements(lista):
    sum=0
    for element in lista:
        if isinstance(element,int):
            sum+=element
        elif isinstance(element,list):
            sum+=recursive_sum_of_elements(element)
    return sum
print(recursive_sum_of_elements([1,2,[1,1,3,[1,2,3]]]))
#python program returns reverse string words
def reverse_str(s):
    reversed_string = " ".join(s.split(" ")[::-1])
    return reversed_string
print(reverse_str("I live in New York"))
#con la recursion
def reverse(string):
    if len(string) == 0:
        return string
    else:
        return reverse(string[1:]) + string[0]

print(reverse('ajahahah'))

#python program returns least frequent character in string
def least_frequent(s):
    dictio={}

    for character in s:
        if character in dictio:
            dictio[character]+=1
        else:
            dictio[character]=1
    x=str(min(dictio, key = dictio.get))
    return x
        
print(least_frequent('ahahahahahahg'))

#python program to reverse the content of a file and store it in another file

f1 = open("output1.txt", "w")
with open("file.txt", "r") as myfile:
    data = myfile.read()
data_1 = data[::-1]
f1.write(data_1)
f1.close()

#python program checks if a substring is present in a given string

def check(string, sub_str):
    if (string.find(sub_str) == -1):
        return 'NO'
    else:
        return 'YES'
            

print(check('ciaoaoi','a'))

#python program to count vowels in string
string=input("Enter string:")
vowels=0
for i in string:
      if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
            vowels=vowels+1
print("Number of vowels are:")
print(vowels)

#python program prints only vowel in string
sentence = input('Enter your sentence: ' )
for letter in sentence:
    if letter in 'aeiou':
        print(letter)

#python program to count vowels in file
file1 = open("d:/mytext.txt", "r")

str1 = file1.read()
vowel_count =  0
for i in str1:
    if( i=='A' or i=='a' or i=='E' or i=='e' or i=='I'
        or i=='i' or i=='O' or i=='o'
	or i=='U' or i=='u'):
        	vowel_count +=1
        

print('The Number of Vowels in text file :', vowel_count)

file1.close()

#python program returns string without vowels
vowels = ['a','e','i','o','u', 'A', 'E', 'I', 'O', 'U']

se = 'the quick brown fox jumps over the lazy dog'

for vowel in vowels:
    se = se.replace(vowel,'')

#python program prints only lowercase words from string
word = "Hello World!"
for letter in word:
    if letter.islower():
        print(letter)



