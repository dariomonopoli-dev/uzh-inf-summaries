#!/usr/bin/env python3

# You can freely adopt this number to print pyramids of different sizes
h = 5

# build a string 
# build a string 
def build_string_pyramid():
    s=''
    for i in range(1, h+1):
        for j in range(1, i+1):
            if i!=j:
                s+=str(j)
                s+="*"            
            else:
                s+=str(j)
                s+='\n'
        
    for i in range(h-1,0,-1):
        for j in range (1, i+1):
            if i!=j:
                s+=str(j)
                s+="*"
              
            else:

                s+=str(j)
                s+='\n'
    return s

print(build_string_pyramid())


#Variante 2: with h given by the user

def build_string_pyramid():
    n=int(input('Tell me how big the Pyramid should be: '))
    s=''
    for i in range(1, n+1):
        for j in range(1, i+1):
            if i!=j:
                s+=str(j)
                s+="*"            
            else:
                s+=str(j)
                s+='\n'
        
    for i in range(n-1,0,-1):
        for j in range (1, i+1):
            if i!=j:
                s+=str(j)
                s+="*"
              
            else:

                s+=str(j)
                s+='\n'
    return s

print(build_string_pyramid())
