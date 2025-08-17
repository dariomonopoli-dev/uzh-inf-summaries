#You are completely free to change this variables to check your algorithm.
num1 = 6 
num2 = 28

#Function to check whether two numbers are friendly pairs or not.
def isFriendlyPair():
    divisors_number_1=0
    divisors_number_2=0
    if num1==num2 or type(num1)!= int or type(num2)!=int:
        return 'Invalid' 
    else:
        for i in range(1, num1+1):
            if num1%i==0:
                divisors_number_1+=i
                abundancy_num_1=divisors_number_1/num1
        for i in range(1, num2+1):
            if num2%i==0:
                divisors_number_2+=i
                abundancy_num_2=divisors_number_2/num2
        if abundancy_num_1==abundancy_num_2:
            return True
        else:
            return False
   

#This line prints your method's return so that you can check your output.
print(isFriendlyPair())