#Task: Check if a Number is Odd or Even
#Objective: Write a Python program that asks the user to enter a number and then tells them if the number is odd or even.

#Instructions:

#Ask the user to input a number.
#Use an if-else statement to check if the number is even or odd.
#A number is even if it’s divisible by 2 (i.e., number % 2 == 0).
#A number is odd if it’s not divisible by 2.
#Print "The number is even" or "The number is odd" based on the result.

#Solution
# Ask the user to enter a number
numb = int(input("Enter a number "))

# Print the entered number
print("You have entered number =", numb)

if numb % 2 == 0:
    print ("The number you entered is EVEN")
else:
    print ("The number you entered is ODD")
