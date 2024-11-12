#Task: Simple Grading System
#Objective: Write a Python program that takes a student's score as input and prints their grade based on the score.

#Grading Criteria:

#If the score is 90 or above, print "Grade: A".
#If the score is 80 to 89, print "Grade: B".
#If the score is 70 to 79, print "Grade: C".
#If the score is 60 to 69, print "Grade: D".
#If the score is below 60, print "Grade: F".
#If the score is negative or above 100, print "Invalid score!".

#Ask for the grade
grade = int(input ("Enter your grade: "))

#Condition
if grade < 0 or grade > 100:
    print ("Invalid score!")
elif grade >= 90:
    print ("Grade: A")
elif grade >= 80:
    print ("Grade: B")
elif grade >= 70:
    print ("Grade: C")
elif grade >= 60:
    print ("Grade: D")
elif grade < 60:
    print ("Grade: F")