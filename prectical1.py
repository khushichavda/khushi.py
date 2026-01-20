Python 3.7.9 (tags/v3.7.9:13c94747c7, Aug 17 2020, 18:01:55) [MSC v.1900 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Simple Interest Program

# Taking input from the user
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time (in years): "))

# Calculating simple interest
simple_interest = (principal * rate * time) / 100

# Displaying the result
print("Simple Interest is:", simple_interest)
Enter the principal amount: 1000
Enter the rate of interest: 5
Enter the time (in years): 2
Simple Interest is: 100.0
# Program to find maximum of two numbers

# Taking input from the user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Finding maximum
if num1 > num2:
    print("Maximum number is:", num1)
else:
    print("Maximum number is:", num2)
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Maximum number is:", max(num1, num2))
for i in range(1, 6):
    print(i)
1
2
3
4
5
# Taking input from the user
text = input("Enter a string: ")

# Finding length
length = len(text)

# Printing result
print("Length of the string is:", length)
print("Welcome to Python Programming!")
Welcome to Python Programming!
text = input("Enter a string: ")
print("First character is:", text[0])
Enter a string: Python
First character is: P
text = input("Enter a string: ")
print("Last character is:", text[-1])
Enter a string: Python
Last character is: n
num = int(input("Enter a number: "))

if num > 0:
    print("The number is Positive")
elif num < 0:
    print("The number is Negative")
else:
    print("The number is Zero")
Enter a number: -5
The number is Negative
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

sum = a + b + c

print("Sum of three numbers is:", sum)
Enter first number: 10
Enter second number: 20
Enter third number: 30
Sum of three numbers is: 60
name = input("Enter your name: ")
print("You entered:", name)
Enter your name: Khushi
You entered: Khushi
