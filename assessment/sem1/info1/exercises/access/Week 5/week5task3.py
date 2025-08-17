from collections import defaultdict

# Dataset contains data that will be reverse indexed
dataset = [
    "Hello world",
    "This is the WORLD",
    "hello again"
 ] 

def reverse_index(dataset):
    lines_dataset=[i.lower().split(' ') for i in dataset]
    lista=[]

    # liste=[]
    # values=[]
    for line in lines_dataset:
        for word in line:
             if word not in lista:
                 lista.append(word)
             else:
                pass
    
    # for index in liste:
    #    list3=values.append(list(enumerate(liste)))
    # for i in range(len(list3)):
    #     values.append(list3[i][0])
    #     return values


    index_dictionary={word: [] for word in lista}
    for word in lista:
        for index, line in enumerate(lines_dataset):
            if word in line:
                index_dictionary[word].append(index)
    return index_dictionary
    # don't forget to return your resulting dictionary

# You can see the output of your function here
print(reverse_index(dataset))