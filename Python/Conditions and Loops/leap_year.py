#Task: Write a Python script that determines if a given year is a leap year.
#Instructions:

#Prompt the user to input a year.
#Use the following rules to check if it's a leap year:
#A year is a leap year if it is divisible by 4.
#However, if the year is divisible by 100, it is not a leap year unless it is also divisible by 400.
#Print whether the year is a leap year or not using if-else.

year = int(input("Enter a year: "))

if year % 4 == 0:
    print ("its a leap year")
else:
    print ("its not a leap year")