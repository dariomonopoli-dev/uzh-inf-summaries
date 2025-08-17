def visualize(records):
    first_class_infobox="== 1st Class =="
    second_class_infobox="== 2nd Class =="
    third_class_infobox="== 3rd Class =="
    first_class_alive=0
    first_class_dead=0
    second_class_alive=0
    second_class_dead=0
    third_class_alive=0
    third_class_dead=0
    records=list(records)[1:]
    for i in records:
        for line in i:
            for classe in range(1,4):
                if line[1]==1 and line[0]:
                    first_class_alive+=1
                elif line[1]==1 and not line[0]:
                    first_class_dead+=1
                if line[1]==2 and line[0]:
                    second_class_alive+=1
                elif line[1]==2 and not line[0]:
                    second_class_dead+=1
                if line[1]==3 and line[0]:
                    third_class_alive+=1
                if line[1]==3 and not line[0]:
                    third_class_dead+=1
    first_class_total=first_class_alive+first_class_dead
    second_class_total=second_class_alive+second_class_dead
    third_class_total=third_class_alive+third_class_dead

    counter_totale_persons=first_class_total+second_class_total+third_class_total  #sum of total passengers

    first_class_total_percentage=round(((first_class_total/counter_totale_persons)*100), 1)    #rounded by 1 decimal numbers
    second_class_total_percentage=round(((second_class_total/counter_totale_persons)*100), 1)
    third_class_total_percentage=round(((third_class_total/counter_totale_persons)*100), 1)
    first_class_total_asterics=round(float(first_class_total_percentage)/5) #counts how many asterics for class 1
    first_class_total_asterics_2=first_class_total_asterics*'*' #multiplies number per *, for example 5*'*'= '*****'
    second_class_total_asterics=(round(float(second_class_total_percentage)/5))
    second_class_total_asterics_2=second_class_total_asterics*'*'
    third_class_total_asterics=(round(float(third_class_total_percentage)/5))
    third_class_total_asterics_2=third_class_total_asterics*'*'
    first_class_alive_percentage=round(((first_class_alive/first_class_total)*100), 1)  #percentage of alive people first class
    second_class_alive_percentage=round(((second_class_alive/second_class_total)*100), 1)
    third_class_alive_percentage=round(((third_class_alive/third_class_total)*100), 1)
    first_class_alive_asterics=(round(first_class_alive_percentage/5))   #asterics for alive people in first class
    second_class_alive_asterics=(round(second_class_alive_percentage/5))
    third_class_alive_asterics=(round(third_class_alive_percentage/5))  
    first_class_alive_asterics_2=first_class_alive_asterics*'*' #number oif asterics per '*', so for example 5*'*'='*****
    second_class_alive_asterics_2=second_class_alive_asterics*'*'
    third_class_alive_asterics_2=third_class_alive_asterics*'*'
    first_class_total_spaces_1=(20-first_class_total_asterics) #20 is the total character space number between first | and last |
    second_class_total_spaces_1=(20-second_class_total_asterics)
    third_class_total_spaces_1=(20-third_class_total_asterics)
    first_class_total_spaces_2=' '*first_class_total_spaces_1 #spaces per number of spaces calculated
    second_class_total_spaces_2=' '*second_class_total_spaces_1
    third_class_total_spaces_2=' '*third_class_total_spaces_1
    first_class_alive_spaces=(20-first_class_alive_asterics)
    second_class_alive_spaces=(20-second_class_alive_asterics) 
    third_class_alive_spaces=(20-third_class_alive_asterics) 
    first_class_alive_spaces_2=' ' * first_class_alive_spaces
    second_class_alive_spaces_2=' ' * second_class_alive_spaces
    third_class_alive_spaces_2= ' '*third_class_alive_spaces
    
    first_class_data_total=f"Total |{first_class_total_asterics_2}{first_class_total_spaces_2}| {first_class_total_percentage}%"
    first_class_data_alive=f"Alive |{first_class_alive_asterics_2}{first_class_alive_spaces_2}| {first_class_alive_percentage}%"
    second_class_data_total=f"Total |{second_class_total_asterics_2}{second_class_total_spaces_2}| {second_class_total_percentage}%"
    second_class_data_alive=f"Alive |{second_class_alive_asterics_2}{second_class_alive_spaces_2}| {second_class_alive_percentage}%"
    third_class_data_total=f"Total |{third_class_total_asterics_2}{third_class_total_spaces_2}| {third_class_total_percentage}%"
    third_class_data_alive=f"Alive |{third_class_alive_asterics_2}{third_class_alive_spaces_2}| {third_class_alive_percentage}%"
    lista=[first_class_infobox, first_class_data_total, first_class_data_alive, second_class_infobox, second_class_data_total, second_class_data_alive, third_class_infobox, third_class_data_total, third_class_data_alive]
    string='\n'.join(lista)
    return string


# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!
_in = []
_in.extend(10 * [(True, 1, 'Some Name', 'female', 38, 71.2833)])
_in.extend(13 * [(False, 1, 'Some Name', 'female', 38, 71.2833)])
_in.extend(22 * [(True, 2, 'Some Name', 'female', 38, 71.2833)])
_in.extend(57 * [(False, 2, 'Some Name', 'female', 38, 71.2833)])
_in.extend(151 * [(True, 3, 'Some Name', 'female', 38, 71.2833)])
_in.extend(276 * [(False, 3, 'Some Name', 'female', 38, 71.2833)])


print(visualize((
    ('Survived', 'Pclass', 'Name', 'Gender', 'Age', 'Fare'),
    _in
)))
