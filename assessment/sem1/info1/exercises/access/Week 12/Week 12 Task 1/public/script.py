#!/usr/bin/python3

from data import words
import string

def words_with_length(length):
    '''this one just serves as an example'''
    return [word for word in words if len(word) == length]

def words_containing_string(s):
    return [word for word in words if s in word]

def words_starting_with_character(c):
    return [word for word in words if word.startswith(c)]

def alphabet():
    alphabet_string = string.ascii_lowercase
    alphabet_list = list(alphabet_string)
    return ''.join(alphabet_list)   

def dictionary():
    return {key: val for key, val in zip(alphabet(), [words_starting_with_character(i) for i in alphabet()])}

def censored_words(s):
    return [len(word) * 'X' if s in word else word for word in words]


