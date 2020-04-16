# Chapter 2: Variables, expressions, and statements

# Exercise 2: Write a program that uses input to prompt a user for their name and then welcomes them.

name = input('Enter your name: ')
print('Hello ' + name)

# Exercise 3: Write a program to prompt the user for hours and rate per hour to compute gross pay.

hours = int(input('Enter Hours: '))
rate = float(input('Enter Rate: '))
pay = hours * rate
print('Pay: ' + str(pay))

# Exercise 4: Assume that we execute the following assignment statements:

width = 17
height = 12.0

n1 = width//2
print(str(n1) + ' : ' + str(type(n1)))

n2 = width/2
print(str(n2) + ' : ' + str(type(n2)))

n3 = height/3
print(str(n3) + ' : ' + str(type(n3)))

n4 = 1 + 2 * 5
print(str(n4) + ' : ' + str(type(n4)))

# Write a program which prompts the user for a Celsius tem- perature, convert the temperature to Fahrenheit, and print out the converted temperature.

## Celsius to Fahrenheit
celsius = float(input('Enter temperature (Celsius): '))
fahrenheit = (celsius * 9/5) + 32
print('Fahrenheit: ' + str(fahrenheit))

## Fahrenheit to Celsius
fahrenheit = float(input('Enter temperature (Fahrenheit): '))
celsius = ((fahrenheit - 32) * 5) / 9
print('Celsius: ' + str(celsius))
