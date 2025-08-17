fyle = open("genetic_code.txt", "r")
genetic_code = {}
for line in fyle:
    line = line.strip()
    line = line.split(" ", 1)
    if line[1] not in genetic_code:
        genetic_code[line[1]] = [line[0]]
    else:
        genetic_code[line[1]].append(line[0])
fyle.close()
sorted_genetic_code = dict(sorted(genetic_code.items(), key=lambda item: item[1]))
print(sorted_genetic_code)
