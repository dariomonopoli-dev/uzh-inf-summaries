

def read_csv(path):
    with open(path, 'r') as f:
        results=[]
        if f=='':
            return results
        else:
            for line in f.readlines():
                if line!='\n':
                    results.append(tuple(line.replace('\n','').split(',')))

        
        return results

# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!
print(read_csv(r"C:\Users\jerry\OneDrive\Desktop\example.csv"))