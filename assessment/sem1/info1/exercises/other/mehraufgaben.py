# def years_100():
#     age=int(input('how old are you'))
#     name=input('who re you')
#     num_copies=int(input('how many times'))
#     till_when=100-int(age)
#     year_future=2021+till_when
#     string = f' Hello {name}, you will turn 100 years old in {year_future}'
#     for i in range(1, num_copies+1):
#         print(string+'\n')
# years_100()

# # def odd_or_even_number():
# #     n=int(input('please enter a number: '))
# #     if n<0:
# #         print("don't do with nbegative numbers")
# #     elif n==0:
# #         print('the number is 0')
# #     elif n%4==0:
# #         print('the number is a multiple of 4')
# # #     elif n%2==1:
# # #         print('the number is odd')
# # #     else:
# # #         print('the number is even')
# # # odd_or_even_number()

# # # def odd_or_even_check():
# # #     n=int(input('please enter a number: '))
# # #     check=int(input('please enter number to divide: '))
# # #     if check!=0:
# # #         if n%check==0:
# # #             print('even division')
# # #         elif n%check==1:
# # #             print('odd division')
# # #     else:
# # #         print('cannot divide by zero')
# # # odd_or_even_check()

# # def exercise_3(l,n):
# #     anotherlist=[]
# #     for i in l:
# #         if i<n:
# #             anotherlist.append(i)
# #     print(anotherlist)
# # exercise_3([1,2,3,4,5,6,7,8,9],8)

# # def print_divisors(n):
# #     for i in range(1,n+1):
# #         if n%i==0:
# #             print(i)
# # print_divisors(8)

# # def exercise_5(l1,l2):
# #     mylist=[]
# #     for i in l1:
# #             if i not in l2:
# #                 mylist.append(i)
# #     for i in l2:
# #             if i not in l1:
# #                 mylist.append(i)
# #     return mylist



# # print(exercise_5([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89],[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]))
# # def palindrome_iterative(s):
# #     stringrev=s[::-1]
# #     if s==stringrev:
# #         print('pali')
# #     else:
# #         print('not pali')
# # palindrome_iterative('ominonanononanonimo')

# # def exercise_7(l):
# #     newlist=[i for i in l if i%2==0]
# #     return newlist
# # print(exercise_7([1,3,5,7,8]))

# # def exercise_8():
# #     player1=input('tell me your play')
# #     player1=player1.lower()
# #     player2=input('tell me your play player 2')
# #     player2=player2.lower()
# #     if player1=='rock' and player2=='scissors':
# #         mesg='player 1 wins'
# #     elif player1=='scissors' and player2=='rock':
# #         mesg='player 2 wins'
# #     elif player1=='scissors' and player2=='paper':
# #         mesg='player 1 wins'
# #     elif player1=='paper' and player2=='scissors':
# #         mesg='player 2 wins'
# #     elif player1=='paper' and player2=='rock':
# #         mesg='player 1 wins'
# #     elif player1=='rock' and player2=='paper':
# #         mesg='player 2 wins'
# #     else:
# #         print("it's a tie")
# #     return mesg
# # print(exercise_8())

# def exercise_9():
#     import random

#     rd = random.randint(1,9)
#     guess = 0
#     c = 0
#     while guess != rd and guess != "exit":
#         guess = input("Enter a guess between 1 to 9")

#         if guess == "exit":
#             break

#         guess = int(guess)
#         c += 1

#         if guess < rd:
#             print("Too low")
#         elif guess > rd:
#             print("Too high")
#         else:
#             print("Right!")
#             print("You took only", c, "tries!")
# input()
# exercise_9()

def exercise_10(l1,l2):
    mylist=[i for i in l1 if i in l2]
    return mylist

print(exercise_10([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89],[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]))

def primality_function(n):
    divisorslist=[]
    for i in range(1,n+1):
        if n%i==0:
            divisorslist.append(i)
    if len(divisorslist)==2:
        return 'is prime'
    else:
        return divisorslist
print(primality_function(13))

def first_last(lista):
    newlist=[]
    newlist.append((lista[0], lista[-1]))
    return newlist
print(first_last([1,2,3,4,5]))

def copy_list(l):
    mylist=[]
    for i in l:
        if i not in mylist:
            mylist.append(i)
    return mylist
print(copy_list([1,2,2,3,4]))

def reverse_words_in_string(s):
    mylist=[]
    line=s.split(' ')
    for i in line:
        mylist.insert(0, i)
        x=' '.join(mylist)
    return x
print(reverse_words_in_string('ciao son dario'))

def reverseWord(w):
  return ' '.join(w.split()[::-1])

print(reverse_words_in_string('ciao sono dario'))

def num_in_list(list, n):
    lista_sortata=sorted(list)
    for i in lista_sortata:
        if n in list:
            return True
        else:
            return False
print(num_in_list([1,2,3,4],6))

def find_max(x,y,z):
    maxim=x
    if y>maxim:
        maxim=y
    elif z>maxim:
        maxim=z
    else:
        maxim=x
    return maxim
print(find_max(5,-2,1))



# def birthday_dictionaries_1():
#     print('Welcome to the birthday dictionary. We know the birthdays of:')
#     dict={'Albert Einstein':'14/03/1879', 'Benjamin Franklin': '01/17/1706', 'Ada Lovelace': '12/10/1815','Donald Trump': '06/14/1946',
#         'Rowan Atkinson': '01/6/1955'}
#     for name in dict:
#         print(name)
#     x=input('what do you want to know the date of?')
#     if x in dict:
#          return f"{x}'s birthday is {dict[x]}."
#     else:
#         return f"Sorry, we don't know {x}'s birthday :/"
# print(birthday_dictionaries_1())


# def boh():
#     mylist=[]
#     string=''
#     n = int(input('oooooooooo: '))
#     for i in range(n):
#         mylist.append(n)
#         n-=1
#     mylist=mylist[::-1]
#     for i in mylist:
#         string+=str(i)
#     return string
# print(boh())

# def split_and_join(line):
#     line=line.split(' ')
#     return '-'.join(line)

# if __name__ == '__main__':
#     line = input()
#     result = split_and_join(line)
#     print(result)
# b = [11,13,15,17,19,21]

# print(b[::2])
# x = ~~~~19
# print(x)
# print(33 == 33.0)
# y = [4, 5,1j]
# print(y.sort())
# a = ['hat', 'mat', 'rat']

# print('rhyme'.join(a))
# l = [1,2,6,5,7,8]
# l.insert(9)
# print(l)
# def rev_func(x,length): 
#    print(x[length-1],end='' '') 
#    rev_func(x,length-1) 
# x=[11, 12, 13, 14, 15] 
# print(rev_func(x,5))
# class P: 
#    def __init__(self): 
#       self.__x=100 
#       self.y=200 
#    def print(self): 
#       print(self.__x, self.y)  
# class C(P): 
#    def __init__(self): 
#       super().__init__() 
#       self.__x=300 
#       self.y=400  
# d = C() 
# d.print()
# num=3
# while True:
#    if (num%0o12 == 0):
#       break
# print(num)
# num += 1
def test1(param):
 return param

def test2(param):
 return param * 2

def test3(param):
 return param + 3

result = test1(test2(test3(1)))
print(result)
def test1(param):
 return str(param)

def test2(param):
 return str(2 * param)

result = test1(1) + test2(2)
print(result)
ints = set([1,1,2,3,3,3,4])
print(len(ints))
def test():
 try:
  return 1
 finally:
  return 2
result = test()
print(result)
mylist=['a', 'aa', 'aaa', 'b', 'bb', 'bbb']
print(mylist[int(-1/2)])
print(list("hello"))
testArr = [11, 22, 33, 22, 11] 
result = testArr[0] 
for iter in testArr: 
 if iter > result: 
  result = iter
print(result)
        