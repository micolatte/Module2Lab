"""
Julie Williams
modlue2lab.py
This app will take the first and last name of a student and their GPA and determine whether or not they will be on the Dean's List or Honor Roll using inputs and while, if, and elif
statements.
"""

while True:
    studentLast = input("What is your last name? ")
    if studentLast == 'ZZZ':
        break

studentFirst = input("What is your first name? ")
studentGPA = float(input("What is your GPA? "))

if studentGPA >= 3.5:
    print("You are on the Dean's List! ")
elif studentGPA >= 3.25:
    print("You are on the Honor Roll! ")
