#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import string #(ER)Importing a module to manipulate strings
# open the text file: 
f = open('relativity.txt')
# read the file and create a list of words (google split function in python):
words = f.read().split() #(ER)Read function will read the text file, return the number of bytes and the split function breaks the texts so each word is its own string.
f.close() #(ER)Closes the opened file
# calculate how many time each word is repeated (using dictionary): #(ER)  
word_counts = {} #(ER)Creates dictionary 
for word in words: #(ER)Goes through each word with the for loop
    word_counts[word] = word_counts.get(word, 0) + 1 #(ER)If the word is present more than once, it will add to the total count.
    #(ER)Get function returns the value of the item with the specified key, if not it will add 0
# create a list of all words:
word_list = list(word_counts.keys())#(ER)Displays all the keys in the dictonary in a list

# sort the list of all words based on how many times they are repeated:
def dict_val(x): #(ER)defining a new function with x as the parameter
    return word_counts[x] #(ER)Returns the values of the dictionary 
word_list.sort(key = dict_val, reverse = True)#(ER)Sorts the list where keys go with the value(dict_val) in reverse order (words with highest frequency to lowest frequency)
# print the top 10 most frequently used words:
print("List of top 10 most frequently used words: ")#(ER)Prints the string
print(word_list[ : 10])#(ER)Print the ten most frequent words
###this doesn't provide much information about the text because all of these are stop words


###second attempt###
#contents = open('relativity.txt').read()   #(ER)Opens text file and returns the number of bytes
#translation_table = {ord(ch) : None  for ch in string.punctuation} #(ER)goes through each character but skips over the punctuation 
#contents = contents.translate(translation_table)   #(ER)translate returns a string where each character is mapped to its corresponding character in the translation table
#words = contents.split()   #(ER)Takes each word and makes it its own string

# create a list of all words in lower case:
lowercase_words = [word.lower() for word in words]  #(ER)Makes all letters in words lowercase 
# open the file containing all of the stop words in English language:
f = open('stopWords.txt')   #(ER)Opens text file 
# read the file create the list of all stop words in English language:
stop_words = f.read().split()   #(ER)Splits the words into separate string in the file and reads it


###remove stop words###
# create the list of non stop words by filtering out the stop words:
non_stop_words = [word for word in lowercase_words if word not in stop_words]   #(ER)loops through every word in lowercase_words and checks if it is in stop_words. If the word is not it will add it to a list non_stop_words
# now calculate the frequency of the non stop words:
word_counts = {}    #(ER)Creates new dictionary 
for word in non_stop_words: #(ER)For loop through words
    word_counts[word] = word_counts.get(word, 0) + 1 #(ER)Counts how many times the word is present in non_stop_words(if word is preent adds 1 if not returns 0)

word_list = list(word_counts.keys())    #(ER)Makes word_list into a list of the keys in word_counts
# sort the words again:
word_list.sort(key = dict_val, reverse = True)  #(ER)Sorts the list where keys go with the value(dict_val) in reverse order (words with highest frequency to lowest frequency)
# prin the top 10 most frequently used words:
print("\nList of top 10 most frequently used non stop words: ") #(ER)Prints the string
print(word_list[ : 10]) #(ER)Prints the ten most frequent words


