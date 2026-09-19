"""
3.1 Write a program to prompt the user for hours and rate per hour
using input to compute gross pay. Pay the hourly rate for the hours
up to 40 and 1.5 times the hourly rate for all hours worked above 40 
hours. Use 45 hours and a rate of 10.50 per hour to test the program 
(the pay should be 498.75). You should use input to read a string and 
float() to convert the string to a number. Do not worry about error 
checking the user input - assume the user types numbers properly.
"""
import sys

try:
    hours = float(input("Enter hours worked: "))
except ValueError:
    print("Error: Please enter a valid number for hours")
    sys.exit()
if hours > 40:
    hours_overtime = hours - 40

try:
    rate = float(input("Enter rate per hour: "))
    rate_overtime = rate * 1.5
except ValueError:
    print("Error: Please enter a valid number for rate")
    sys.exit() 


if hours <= 40:
    payment = hours * rate
    print("Payment for hours worked: ", payment)
else:
    payment = (40 * rate) + (hours_overtime * rate_overtime)
    print(payment)
