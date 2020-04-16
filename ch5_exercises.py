# Chapter 5: Iteration

## Exercise 1: Write a program which repeatedly reads numbers until the user enters “done”. Once “done” is entered, print out the total, count, and average of the numbers. If the user enters anything other than a number, detect their mistake using try and except and print an error message and skip to the next number.

count = 0
total = 0.0
while True:
    number = input('Enter a number: ')
    if number == 'done':
        break
    try:
        num = float(number)
    except:
        print('Invalid input')
        continue
    count = count + 1
    total = total + num
    average = total/count
print(total,count,average)

## Exercise 2: Write another program that prompts for a list of numbers as above and at the end prints out both the maximum and minimum of the numbers instead of the average.

max_num = None
min_num = None
while True:
    number = input('Enter a number: ')
    if number == 'done':
        break
    try:
        num = float(number)
    except:
        print('Invalid input')
        continue
    if max_num is None or num > max_num :
        max_num = num
    if min_num is None or num < min_num :
        min_num = num
print(max_num, min_num)
