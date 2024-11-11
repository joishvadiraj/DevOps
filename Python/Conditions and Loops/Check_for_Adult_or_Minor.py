#Task: Check for Adult or Minor
#Objective: Write a Python program that asks the user to enter their age and then tells them whether they are an adult or a minor.

#Instructions:

#Ask the user to input their age.
#Use an if-else statement to check:
#If the age is 18 or older, print "You are an adult".
#If the age is less than 18, print "You are a minor".

#Solution
#Ask for the age
age = int(input("Enter your age: "))

#Condition
if age >= 18:
    print("You are an adult")
elif age < 0:
    print("Invalid age!")
else:
    print("You are a minor")