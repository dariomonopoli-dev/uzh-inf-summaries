#!/usr/bin/env python3

# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!
def preprocess(records):
    survived_values = ['true','t','yes','survived','Alive','alive','Yes','T','True','Survived']
    non_survived_values = ['false','False','no','No','f','F','dead','survived=dead','Dead']
    class_values=[1,2,3]
    male_values= ['male','Male','m','M']
    female_values = ['female','Female','f','F']
    invalid_values=['','undefined','Undefined','unknown','Unknown']
    lista=[]
    first_element=records[0]
    for i in records[1:]:
        if i[0] in invalid_values:
            continue
        elif i[0] in survived_values:
            survived = True
        elif i[0] in non_survived_values:
            survived = False
        else:
            print(i[0])
        if i[1] in invalid_values:
            continue
        elif int(i[1])==1 or int(i[1])==2 or int(i[1])==3:
            Pclass=int(i[1])
        else:
            continue
        if i[2] in invalid_values:
            continue
        else:
            name = i[2]
        if i[3] in invalid_values:
            continue
        elif i[3] in male_values:
            gender = 'male'
        elif i[3] in female_values:
            gender = 'female'
        else:
            print(i[3])
        if i[4] in invalid_values or float(i[4])<=0 or float(i[4])> 100:
            continue
        else:
            age = float(i[4])
        if i[5] in invalid_values or float(i[5])<0:
            fare = float(25)
        else:
            fare = float(i[5])
        lista.append((survived, Pclass, name, gender, age, fare))
    finale = (first_element, lista)
    return finale

           

        



# The following part calls the function and prints the return
# value to the Console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!

# Investigate the 'titanic.csv' file before you attempt a submission.
# You might want to download the file to your machine and open it with the function that you have written in Task 1.
# The following example is not complete.

titanic = [
    ('Survived', 'Pclass', 'Name', 'Gender', 'Age', 'Fare'),
    ('no', '3', 'Braund Mr. Owen Harris', 'male', '22', '7.25'),
    ('no', '3', 'Braund Ms. Maria', 'Female', '22', ''),
    ('Yes', '1', 'Cumings Mrs. John Bradley (Florence Briggs Thayer)', 'F', '38', '71.28'),
    ('', '3', 'Vander Planke Miss. Augusta Maria', 'female', '', ''),
    ('Dead', '4', 'Lennon Mr. Denis', 'male', '13', '15.5')]

print(preprocess(titanic))
