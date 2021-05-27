
# File: module2_assignment_Keeley.py
# Base script copied from: pyScript19.py
# CS 5010
# Module 2 Live Session Assignment (Python version: 3)
# Nicholas Keeley, ngk3pf
'''
# Worked with Drew Pearson, dp6tk. We both built our own modules to enhance 
individual understanding, and then compared to optimize efficiency.
'''
## Description
'''
This program defines class Student, allowing for the creation of Student type
objects. Each Student instance possesses a "name", "id", and "grades" attribute.
The program then tests a series of functions defined within the class Student
and ultimately produces an average of each student's grades.
'''


class Student:
    # fields: name, id, grades(a list)
    
    def __init__(self, name, id, grades):  # constructor
        self.name = name
        self.id = id
        self.grades= grades
  
    def addGrade(self, grade): # add the grade to the list of grades
        self.grades.append(grade)
    
    def showGrades(self): # displaying the grades
        grds = '' # empty string
        for grade in self.grades: # Loop through grades list
            grds += str(grade) + ' '  # assign each grade to the string grds
        return grds
    
    def __str__(self):
        return str(self.name) + " " + str(self.id) + " " + str(self.showGrades())

    def average(self):
        total=0
        for i in range(len(self.grades)):
            total += self.grades[i]
        avg = total/len(self.grades)
        return avg
             
#==================================================
    
student1 = Student("Nick", "ngk3pf", [40, 80, 90])
print(student1) # Output: Nick ngk3pf 40 80 90 
print(student1.average()) # Output: 70.0
student1.addGrade(100)
print(student1.showGrades()) # Output: 40 80 90 100 
print(student1.average()) # Output: 77.5

student2 = Student("John", "js333", [1, 0.43])
print(student2) # John js333 1 0.43 
print(student2.average()) # Output: 0.715
student2.addGrade(90)
print(student2.showGrades()) # Output: 1 0.43 90 
print(student2.average()) # Output: 30.47666666666667

# for index, item in enumerate(my_list):