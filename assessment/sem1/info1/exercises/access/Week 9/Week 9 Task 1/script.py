#!/usr/bin/env python3

# The signatures of this class and its public methods are required for the automated grading to work. 
# You must not change the names or the list of parameters. 
# You may introduce private/protected utility methods though.
class ProfanityFilter:
    def __init__(self, keywords, template):
        self.__keywords = sorted(keywords, key=len, reverse=True)
        self.__template = template


    def filter(self, msg):
        for swear_word in self.__keywords:
            while msg.lower().find(swear_word) != -1:
                index = msg.lower().find(swear_word)
                formula = len(swear_word) // len(self.__template)
                rest = len(swear_word) % len(self.__template)
                msg = msg.replace(msg[index: index + len(swear_word)], (formula * self.__template + self.__template[:rest]))
        return msg



if __name__ == '__main__':
    f = ProfanityFilter(["duck", "shot", "batch", "mastard"], "?#$")
    offensive_msg =  "absHOtc DebATChfghi AaaMaStard jklMnoDUCK duck sHOt"
    clean_msg = f.filter(offensive_msg)
    print(clean_msg)  # abc defghi ?#$?#$? jklmno
    
    


