#!/usr/bin/env python3

# This signature is required for the automated grading to work. 
# Do not rename the function or change its list of parameters.
def analyze(posts):
    dictionary={}
    lista=[]
    numbers="0123456789"
    for line in posts:
        split_space=line.replace('.','').replace('-', '').split()
        for word in split_space:
            if '#' in word:
                    altre_word = word.split('#')
                    del altre_word[0]
                    for word in altre_word:
                        end=len(word)
                        if end!=0:
                            if not word[0] in numbers:
                                    if word not in dictionary:
                                        dictionary[word]=1
                                    else:
                                        dictionary[word]+=1                                    
                                    

                    

    return dictionary
        # print(parola_split)


# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!
posts = [
    "hi#weekend  ",
    "good morning #zu#rich #limmat",
    "spend my #weekend in #zurich",
    "#zurich <3",
    "#1u",
    ".#c"
    "#",
    '#1ciao'
    ".#c.",
    "zurich-cool"]
    
print(analyze(posts))