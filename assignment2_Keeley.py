# File: assignment2_Keeley.py
# CS 5010
# In-Class Assignment 2: Python (Python 3)
# Nicholas Keeley, ngk3pf


'''
This program takes a sentence of words and prints them with their respective
word lengths. It then attempts to sort the tuples by word length unsucessfully.
'''


# Create sentence and separate words.

sentence = "The first language I ever learned was Java because I was told Java is the best language"
words = sentence.split(" ")

# List comprehension returning word and length of word.
words = [(word,len(word)) for word in words]

f = lambda x,y: x+y
print(f(2, 3))

# Print.
print(words)




'''
# Sort tuples by word length.
max = words[1][1]
for word in words:
    if max < word[1]:
        max = word
        
        
max = [word for word in words if max[1] < word[1]]
print(max)

# This addresses the correct word length value in tuple.
print([words[2][1]])
'''


