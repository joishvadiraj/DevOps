#Task: Grade Calculator
#Write a program that asks the user for a numerical score (0–100) and then assigns a grade based on the score. Use if-else conditions to print the correct grade:

#Grading Scale
#90–100: Grade A
#80–89: Grade B
#70–79: Grade C
#60–69: Grade D
#Below 60: Grade F
#Steps:
#Prompt the user to enter a score.
#Use if-else conditions to determine which grade to assign.
#Print the assigned grade.

score = int(input("Enter your score: "))
if score > 100 or score < 0:
    print ("Invalid score")
elif score >= 90:
    print ("Grade A")
elif score >= 80:
    print ("Grade B")
elif score >= 70:
    print ("Grade C")
elif score >= 60:
    print ("Grade D")
elif score < 60:
    print ("Grade F")