# Chapter 4: Functions

## Exercise 1: Run the program on your system and see what numbers you get. Run the program more than once and see what numbers you get.

import random 

random.randint(5, 10)
t = [1, 2, 3]
random.choice(t)

## Exercise 2: Move the last line of this program to the top, so the function call appears before the definitions. Run the program and see what error message you get.

def print_lyrics():
    print("I'm a lumbrejack, and I'm okay.")
    print('I sleep all night and I work all day.')
print_lyrics()

def repeat_lyrics():
    print_lyrics()
    print_lyrics()
repeat_lyrics()

# Output:
# Traceback (most recent call last):
#   File "exercises_4.py", line 10, in <module>
#     repeat_lyrics()
# NameError: name 'repeat_lyrics' is not defined

## Exercise 3: Move the function call back to the bottom and move the definition of print_lyrics after the definition of repeat_lyrics. What happens when you run this program?

# Output: 
# I'm a lumbrejack, and I'm okay.
# I sleep all night and I work all day.
# I'm a lumbrejack, and I'm okay.
# I sleep all night and I work all day.
# I'm a lumbrejack, and I'm okay.
# I sleep all night and I work all day.

## Exercise 5: What will the following Python program print out?

def fred(): print("Zap")
def jane(): print("ABC")
jane()
fred()
jane()

# Output:
# ABC
# Zap
# ABC

## Exercise 6: Rewrite your pay computation with time-and-a-half for over- time and create a function called computepay which takes two parameters (hours and rate).

hours = float(input('Enter Hours: '))
rate = float(input('Enter Rate: '))
def computepay(hours, rate):
    otpay = ((hours - 40) * rate) * 1.5
    computepay = (40 * rate) + otpay
    return computepay
pay = computepay(hours, rate)
print('Pay: ' + str(pay))

## Exercise 7: Rewrite the grade program from the previous chapter using a function called computegrade that takes a score as its parameter and returns a grade as a string.

try:
    score = float(input('Enter score: '))
    def computegrade(score):
        if score < 0.0 or score > 1.0:
            print('Bad score')
        else:
            if score >= 0.9:
                print('A')
            elif score >= 0.8:
                print('B')
            elif score >= 0.7:
                print('C')
            elif score >= 0.6:
                print('D')
            else:
                print('F')
    computegrade(score) 
except:
    print('Bad score')
