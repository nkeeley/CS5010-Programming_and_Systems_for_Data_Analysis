# File: homework2_keeley.py
# CS 5010
# Homework: Python (Python version: 3)
# Nicholas Keeley, ngk3pf

'''
Description: This program contains seven miniscripts conducting a variety of tasks.
'''
'''
### Q1: Dictionary basics (2 pts)

# Sets up dictionary with favorite news sources, keyed with simulated integer label.
test_dictionary = {1:"NYT", 2:"WSJ", 3:"WIRED",4:"ZeroHedge",5:"BBC World",
                   6:"TechCrunch", 7:"Peoples' Daily", 8: "Xinhua", 9:"LiveLeaks",
                   10:"War on the Rocks"}

# Retrieve three different values using keys. Prints them for display.
print(test_dictionary[4]) # Output: ZeroHedge
print(test_dictionary[1]) # Output: NYT
print(test_dictionary[10]) # War on the Rocks


### Q2: Getting user input: (2 pts)

# Sets up variables through user input: name, number input 1, and number input 2.
name = input("What's your name?: ")
inp1 = float(input("Please enter your first number: "))
inp2 = float(input("Please enter your second number: "))

# Multiply the two inputted numbers together. Save as result1.
result1 = inp1*inp2
print(result1)

# Display output using str.format() method and variable inputs.
print("Hi, {}! Multiplying {} and {} is: {}".format(name, inp1, inp2, result1))
# alt method: print("Hi, %s! Multiplying %f and %f is: %.3f" % (name, inp1, inp2, result1)) 


### Q3: Converting code to use a while loop: (3 pts)

# Prompt to begin the guessing game, sets up guesses variable to track how many are left.
answer = "Watson"
print("Here is a guessing game. You get three tries.")
print("What is the name of the computer that played on Jeopardy?")
guesses = 3

# Create a while loop contingent on guesses left. Loop ends once guesses dip below 1.
while (guesses > 0):
    # Executed for every iteration.
    response=input() 
    
    # Creates condition for success! Breaks out of loop.
    if response == answer:
        print("That is right!")
        break
    
    # If not success, creates three distinct scenarios reliant on guesses left.
    else:
        if guesses == 3:
            print("Sorry. Guess again: ")
            guesses-=1
            continue # Continues to next loop iteration without executing code below.
        if guesses == 2:
            print("Sorry. One more guess: ")
            guesses-=1
            continue # Continues to next loop iteration without executing code below.
        
        # Final condition: You lost!
        print("Sorry. No more guesses. The answer is " + answer + ".")
        guesses -= 1 # Crucial otherwise loop will continue.

### Q4: Counting each of the vowels: (3 pts)

# Set up string to iterate through and storage variables for vowels.
sentence = "are you suggesting coconuts migrate"
a_num = 0
e_num = 0
i_num = 0
o_num = 0
u_num = 0

# Set up for-loop to check for vowels and update respective storage variables.
for letter in sentence:
    if letter == "a":
        a_num+=1
    if letter == "e":
        e_num+=1
    if letter == "i":
        i_num+=1
    if letter == "o":
        o_num+=1
    if letter == "u":
        u_num+=1

# Display the number of vowels in a given sentence.       
print("There are {} a's, {} e's, {} i's, {} o's, and {} u's in this sentence.".format(
    a_num, e_num, i_num, o_num, u_num))

### Q5: Length of all the words in a sentence (based on exercise in pyScript13.py) (3 pts)

# Create sentence without punctuation to parse into words
sentence2 = "Perseverance defeats all obstacles for when a determined man sets out to do something the battle is half won"

# Split using spaces.
words2 = sentence2.split(" ")

# List comprehension to separate words into tuples with the word and word length as values.
words2 = [(word, len(word)) for word in words2]

# Sort words based on word length, then print.
words2_new=sorted(words2, key=lambda x: x[1])
for word in words2_new:
   print("{}, {}\n".format(word[0], word[1]))


### Q6: Map-Filter-Reduce examples: (3 pts)

## Example 1: Mimic map and square every number in a list.

# Define square, even, and sum functions for lower order functions.
def square (x):
    return x*x
def even(x):
    if x % 2 == 0:
        return True
    else:
        return False
def sum(x,y):
    return x + y

numbers = [1,2,3]
print(numbers)
# For loop iterates through every value in a given list and squares it, overwriting to same list.
for i in range(len(numbers)):
    numbers[i]=square(numbers[i])
print(numbers)

## Example 2: Mimic filter and filter out the even nubmers in a list

numbers = list(range(1,11))
new_list = []
j=0
print(numbers)
# For loop iterates through every value in a given list. If even, stores into new list. 
for i in range(len(numbers)):
    if even(numbers[i]):
        # Reads even number into new list.
        new_list.append(numbers[i])
print(new_list)

## Example 3: Mimic reduce function and adds every value in list to one sum.

numbers = list(range(1,11))
print(numbers)
sum2 = 0

# Iterate through values in list and add them together in the sum variable.
for i in range(len(numbers)):
    print(numbers[i])
    sum2 = sum(sum2, numbers[i])
    print(sum2)
    
print("The sum of the range is " + str(sum2))
'''

### Q7: Classes and Inheritance: (4 pts)

# Base class.
class ACCOUNT:
    # Constructor method for base class.
    # accountNumber (string)
    # balance (float)
    def __init__(self, accountNumber, balance):
        self.accountNumber = accountNumber
        self.balance = balance
    # String constructor to print values easily.
    def __str__(self):
        return "Account number " + str(self.accountNumber) + "\nBalance: " + str(self.balance)

# Derived class taking base class as argument.
class CHECKING(ACCOUNT):
    # Derived class constructor.
    # fee (int)
    def __init__(self, accountNumber, balance, fee):
        # Call base class constructor method.
        ACCOUNT.__init__(self, accountNumber, balance)
        self.fee = fee

    
    # Derived class string constructor.
    def __str__(self):
        new_strng = "Account type: Checking"
        # Calling base class string constructor.
        old_strng = ACCOUNT.__str__(self)
        return new_strng + "\n" + old_strng
    
    # Get fee method. Returns fee.
    def getFee(self):
        return self.fee
    
    # Deposit method. Adds amount to balance but doesn't return anything.
    def deposit(self, amount):
        self.balance += amount
    
    # Withdraw method. Makes sure you have enough balance to withdraw, then takes
    # fee and withdrawal amount out of account.
    def withdraw(self, amount):
        if self.balance < amount:
            print("Insufficient funds!")
        else:
            self.balance = self.balance - amount - self.fee

#============================================================================#
check1 = CHECKING("1234", 500, 0.50)
print(check1)
check1.withdraw(100)
print(check1)
check1.deposit(200)
print(check1)
act1 = CHECKING("1234", 500, 1)
print(act1.accountNumber)

print("1234"[1:])

nameLst = [ 'Bob', 'JOHN', 'alice', 'jaN', 'CLAYTON', 'N', 'May' ] 
r = [name[0].upper() + name[1:].lower() for name in nameLst if len(name) > 1]

print(r)


