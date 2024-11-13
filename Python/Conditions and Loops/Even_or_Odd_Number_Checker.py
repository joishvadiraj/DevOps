#Task: Even or Odd Number Checker
#Write a program that asks the user to enter an integer and then checks if the number is even or odd. Use if-else conditions to determine and print the result.

#Steps:
#Prompt the user to enter an integer.
#Use if-else conditions to check if the number is even or odd.
#Print whether the number is "Even" or "Odd".

numb = int(input("Enter the number: "))
if numb % 2 == 0:
    if numb % 2 == 4:
        print ("The number is multiple by 4")
    else:
        print ("The number is Even")
else:
    print ("The number is ODD")