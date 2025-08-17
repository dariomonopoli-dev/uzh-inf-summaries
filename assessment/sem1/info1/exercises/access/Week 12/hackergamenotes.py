
import random
length = 6
num_words = 8
attempts = 4
with open('words.txt', 'r') as f:
    contents = f.read().splitlines()
print(contents)
fixed_length_words = [word.upper() for word in contents if len(word) == length]
#esiste anche la dict comprehension:
l = [1,2,3,4,5]
res = {x: x*2 for x in l if x>3}
print(res)

words = random.sample(fixed_length_words, num_words)
password = random.choice(words)

while attempts:
    guess = input('> ')
    if guess==password:
        print('ACCESS GRANTED')
        break
    else:
        print('ACCESS DENIED')
    attempts-=1
    matching = sum([1 for p, g in zip(password, guess) if p==g])
    print(f'MATCHING: {matching}/{attempts}')
    print(f'{attempts} ATTEMPTS REMAINING')
    if attempts==0:
        print('OUT OF ATTEMPTS')
print('ciao', end='')  #end leere stringa printa ttutto su una stringa nella shell


