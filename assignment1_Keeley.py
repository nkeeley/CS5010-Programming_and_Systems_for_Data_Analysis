#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# File: assignment1_Keeley.py, myOutput.txt
# CS 5010
# In-Class Assignment 1: Python (Python 3)
# Nicholas Keeley, ngk3pf

'''
Creates a dictionary utilizing user-input keys and values. Keys are stripped
to lastname-firstname format, and values are integers representing the age of
the person represented by the key. Finally, the program outputs a .txt file of
the dictionary.
'''

# Import sys library.
import sys


# Prompt user inputs and assigns to global variables.
last_name = input("Last name?: ")
first_name = input("First name?: ")
age = input("Age?: ")

# TEST: GOOD.

# Strip whitespace, concatenate names, change age to integer type.
last_name.strip()
first_name.strip()
age.strip()

name = last_name + "-" + first_name

age = int(age)

# TEST: GOOD.

# Load variables into a dictonary.
db = {name:age}

# TEST: GOOD

# Iterate three more times.
i = 0
while (i < 3):
    last_name = input("Last name?: ")
    first_name = input("First name?: ")
    age = input("Age?: ")

    # TEST: GOOD.
    
    # Strip whitespace, concatenate names, change age to integer type.
    last_name.strip()
    first_name.strip()
    age.strip()
    
    name = last_name + "-" + first_name
    
    age = int(age)
    
    # Load variables into a dictonary.
    db[name] = age
    i=i+1

# TEST: GOOD]

print(db)

# Create .txt file.
original = sys.stdout
sys.stdout = open("myOutput.txt", 'a')
print(db)
sys.stdout = original




