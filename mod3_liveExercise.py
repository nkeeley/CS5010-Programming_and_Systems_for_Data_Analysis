# File: module3_liveExercise.py
# CS 5010
# Module 03: Live Session Exercise: Exception Handling (Python version: 3)
# Nicholas Keeley, ngk3pf

## Question 1
''' 
When the designated code was executed, an IOError populated instead of a
FileNotFoundError. This is because the IOError is a parent class of the
FileNotFoundError sub class, and both exception handlers will capture a 
"file not found." Because the IOError is a hierarchically higher subclass 
within the Exception base class, it caught the error first and executed its
code as the designated error handler. This could have been avoided by explicitly
placing the hierarchically lower subclass FileNotFoundError ahead of the IOError
subclass within the program. Note: none of the rest of the code in the "try"
code block ran after the excetion handler took over.
'''

## Question 2

'''
This program possesses a series of scenarios in which common errors occur.
Each common error is "caught" with an exception handler. The exception handlers
are nested to facilitated inheritance/so that none of the code is unreachable.
'''

try:
    
    rand_int = int(input("What's your integer?: ")) 
    print(rand_int)
    
    if rand_int < 5:
        new_num = int(10/rand_int)
        print(new_num)
    else:
        new_num = 1/rand_int
        print(new_num)
    
    word = "wheaties."
    for i in range(new_num):
        print(word[i])
    
    file_name = input("Insert file name: ")
    file = open(file_name, "r")
    
except FileNotFoundError:
    print("File not found.") # If input works, but file name inaccessible.

except ZeroDivisionError:
    print("Can't divide number by zero.") # If input 0.
    
except IOError: # comment out the FileNotFoundError and run same error to catch this.
    print("Input/Output error found.") # Catches IO errors. This is a parent class of FileNotFoundError.
    
except ValueError:
    print("Value Error.") # Value incompatible with operation. If you input string.

except ArithmeticError: # Catches arithmetic error. This is a parent class of ZeroDivisionError.
    print("Arithmetic error found.") 
    
except TypeError:
    print("Type error found.") # Input 100.

except Exception:
    print("You triggered an error not listed above.") # If input is 1.

finally:
    print("\nCongrats, you made it out of the try-except-finally chain. This will print regardless.")


