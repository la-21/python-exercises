# Chapter 6: Strings

## Exercise 1: Write a while loop that starts at the last character in the string and works its way backwards to the first character in the string, printing each letter on a separate line, except backwards.

index = 0
fruit = 'watermelon'
while index < len(fruit):
    index = index - 1
    fruity = (fruit[index])
    print(fruity)

## Exercise 2: Given that fruit is a string, what does fruit[:] mean?

# e.g. 
fruit = 'watermelon'
print(fruit[:])
# output: watermelon

## Exercise 3: Encapsulate this code in a function named count, and gen- eralize it so that it accepts the string and the letter as arguments.

word = 'banana' 
count = 0
for letter in word:
    if letter == 'a': 
        count = count + 1
print(count)

word = input('Enter a word: ')
letter = input('Enter a letter you want to count: ')
def count():
    count = 0
    for ltr in word:
        if ltr == letter:
            count = count + 1
    print(count)
count()

## Exercise 4: There is a string method called count that is similar to the function in the previous exercise. Read the documentation of this method at:
## https://docs.python.org/library/stdtypes.html#string-methods
## Write an invocation that counts the number of times the letter a occurs in “banana”.

fruit = 'banana'
letter = 'a'
count = fruit.count(letter)
print('The count of `' + letter + '` on word `' + fruit + '` is: ', count)

## Exercise 5: Take the following Python code that stores a string:
## str = 'X-DSPAM-Confidence:0.8475'
## Use find and string slicing to extract the portion of the string after the colon character and then use the float function to convert the extracted string into a floating point number.

str1 = 'X-DSPAM-Confidence:0.8475'
colonstr1 = str1.find(':')
endstr1 = len(str1)
floatstr1 = float(str1[colonstr1+1:endstr1])
print(floatstr1)

## Exercise 6: Read the documentation of the string methods at https://docs.python.org/library/stdtypes.html#string-methods. You might want to experiment with some of them to make sure you understand how they work. strip and replace are particularly useful.
## The documentation uses a syntax that might be confusing. For example, in find(sub[, start[, end]]), the brackets indicate optional arguments. So sub is required, but start is optional, and if you include start, then end is optional.

# str.replace(old, new[, count])

str2 = 'this is a string and I want this to be replaced with this'
print(str2.replace('this','that',3))

# with capital letter
str3 = 'This is a string and I want this to be replaced with this'
str3 = str3.lower()
print(str3.replace('this','that',3))

# str.strip([chars])
comment = '#.......... Chapter 6 Section 6.5.1 String Methods ... '
print(comment.strip('.#! '))

