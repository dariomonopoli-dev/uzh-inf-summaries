
def gender_class_rates(dataset):
    try:
        dataset[1][0][5]
        pass
    except IndexError:
        return None
    #if not dataset[1][0][6]: return
    invalid_values=[None, None, None, None, None, None]
    counter=0
    for i in range(1, 4):
        for line in dataset[1]:
            if(line[1]==i and line[3]=="male"):
                if invalid_values[i-1]==None: invalid_values[i-1]=1
                else: invalid_values[i-1]+=1
            if(line[1]==i and line[3]=="female"):
                if invalid_values[i+2]==None: invalid_values[i+2]=1
                else: invalid_values[i+2]+=1
    for elemento in invalid_values:
        if elemento!=None: counter+=elemento
    for idx, value in enumerate(invalid_values):
        if value!=None:
            invalid_values[idx]=round((value/counter*100), 1)
    prima=invalid_values[:3]
    dopo=invalid_values[3:]
    return (tuple(prima), tuple(dopo))
print(gender_class_rates((
    ('Survived', 'Pis', 'Name', 'Gender', 'Age', 'Fare'),
    [
        (True, 1, 'Cumings Mrs. John Bradley (Florence Briggs Thayer)',
         'female', 38, 71.2833),
        (False, 3, 'Heielementoelementoinen Miss. Laina', 'female', 26, 7.925)
        # ...
    ]
)))
