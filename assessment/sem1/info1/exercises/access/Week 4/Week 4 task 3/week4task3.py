#!/usr/bin/env python3

import os

# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!
def process_data(path_reading, path_writing):
    if not os.path.exists(path_reading):
        return False
    else:
        filecondata=open(path_reading, 'r')
        ilmiodata=filecondata.read().split('\n')
        listadata=''
        for i in ilmiodata:
            if i=='Name':
                listadata='Firstname,Lastname'
            elif i=='':
               listadata=listadata + '\n' + ','
            elif ' ' in i:
                if ';' in i:
                    splitta=i.split(';')
                    i=splitta[1].strip() + ' ' + splitta[0]
                    splitta=i.split(' ')
                    i=','.join(splitta)
                    listadata=listadata+'\n'+i
                else:
                    splitta=i.split(' ')
                    i=','.join(splitta)
                    listadata=listadata+'\n'+i
            else:
                pass
    file_processato=open(path_writing, 'w')
    if ilmiodata[0]=='':
        file_processato.close()
    else:
        file_processato.write(listadata)
    file_processato.close()              



# The following line calls your solution function with the provided input file
# and then attempts to read and print the contents of the resulting output file.
# You do not need to modify these lines.
INPUT_PATH = "public/my_data.txt"
OUTPUT_PATH = "public/my_data_processed.txt"
process_data(INPUT_PATH, OUTPUT_PATH)
if os.path.exists(OUTPUT_PATH):
    with open(OUTPUT_PATH) as resultfile:
        print(resultfile.read())
else:
    print("No output file exists")

