from typing import Hashable


def hashtag_pyramid_1(size):
    hashtag_string=''
    for i in range(1,size+1):
        for j in range(1,i+1):
            if j==i:
                hashtag_string+='#'
                hashtag_string+='\n'


            else:
                hashtag_string+='#'
    for i in range(size-1, 0, -1):
        for j in range(1,i+1):
            if j==i:
                hashtag_string+='#'
                hashtag_string+='\n'

            else:
                hashtag_string+='#'

                
    return hashtag_string
print(hashtag_pyramid_1(4))
print('space between two exercises')
print(' ')
print('Horizontal hashtag pyramid')
def horizontal_pyramid(size):
    s=''
    m = (2 * size) - 2
    for i in range(1, size):
        for j in range(1, m+1):
            s+=' '
        m=m-1
        for j in range(1, i + 1):
            s+='#'
            s+=' '
        s+='\n'
    return s
print(horizontal_pyramid(10))
def hashtag_pyramid_3(size):
    s=''
    for i in range(1, size+1):
        for j in range(1, i + 1):
            s+='#'
            s+=' '
            
        s+='\n'

    for i in range(size, 0, -1):
        for j in range(0, i - 1):
            s+='#'
            s+=' '
        
        s+='\n'
    return s
print(hashtag_pyramid_3(20))
def hashtag_pyramid_4(size):
    hashtag_string=''
    for i in range(1,size-1):
        hashtag_string+=(i*'#')+'\n'
        hashtag_string+=((i+2)*'#')+'\n'
    for i in range (size-2,1,-1):
        hashtag_string+=(i*'#')+'\n'
        hashtag_string+=((i+1)*'#')+'\n'
    return hashtag_string
print(hashtag_pyramid_4(4))
def sum_two_numbers(a,b):
    if b:
        sum=a+b
        return sum
    else:
        return a+1
print(sum_two_numbers(2,''))
def reverse(string):
    if len(string) == 0:
        return string
    else:
        for i in range(len(string)):
            return reverse(string[i])
print(reverse('hahahahahahj'))
    
