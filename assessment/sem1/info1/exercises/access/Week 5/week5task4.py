wa_nrs = ["0781111119", "0792653913", "0797763139", "0792793193", "0781139022", "0764320165"]


# This signature is required for the automated grading to work. 
# Do not rename the function or change its list of parameters.
def get_possible_nrs(n):
    possible_nrs_for_juliet = []
    for index in range(len(n)):
        for j in range(10):
            j=str(j)
            number=n[:index]+j+n[index:] 
            if index==max(range(len(n))):
                number=n[:index+1]+j
            possible_nrs_for_juliet.append(number)
    wa_nrs_set=set(wa_nrs)
    what_in_common=wa_nrs_set.intersection(possible_nrs_for_juliet)
    return list(what_in_common)
    # listadelcommon=list(what_in_common)
    # x=listadelcommon
    # Don't forget to return your result

# For this particular number, the function should find the
# last element in wa_nrs
print(get_possible_nrs("076432165"))