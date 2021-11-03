# this is a comment

"""
if I wanted to make a multiline comment, this is how I do it
var = 4
"""

#create a variable in python

my_fav_console = 'Nintendo 64\n'

print(my_fav_console)

#Python Syntax

#def (functions)
#if, elif, else (conditional statements)
#for, while (loops)
#Class (classes)

#Let's do some examples of seeint variables, an if statement and printing

x = 10 
if x > 5:
    print ("x is greater than 5\n")
else:
    print("x is not greater than 5\n")

y = 20
if y > 20:
    print ("Y is greater than 20\n")
else:
    print ("Y is not greater than 20\n")

#Pass - Pass can be used to fill up space in a code block to run code when we dont know what to put yet
#nothing happens when pass is executed. It is a null operation

class EmptyClass:
    pass

for val in "my_string":
    pass

#Data Types

#Primitive Data Types - Basic building blocks of Python. Booleans, Integers and Strings
###Booleans
is_hungry = True
has_freckles = False

if is_hungry == True:
    print ("I am hungry.\n")

if has_freckles == True:
    print ("I have freckles")
else:
    print ("I do not have freckles. I am at line 57 as a marker\n")

###Integers
my_fav_number = 64
my_second_fav_number = 128
age = 32
weight = 195.24
dogs_weight = 20

print (my_fav_number + my_second_fav_number, "\n")
print (weight + dogs_weight, '\n')

###Strings
favorite_vg = "ghosts of tsushima\n"
print(favorite_vg.title())

##side note - if you want it capitalized, add .title() to the print function

###Composite Data Types - Tuples, Lists and Dictionaries
##Tuples - a type of data type that is immutable. A list that holds a group of variables

dog = ("toogie", "sasha", "wynston")
print(dog)
print(dog[2])
print(dog[1:3])
print()

##Lists a type of data that is mutable and can hold a group of values
list_of_consoles = ["N64", "SNES", "Sega Genesis", "Playstation"]
print(list_of_consoles)
print(list_of_consoles[0:3])
list_of_consoles.append("Game Boy")
print(list_of_consoles)
list_of_consoles.pop()
print(list_of_consoles)
list_of_consoles.pop(1) #This is how you target what to pop. I have targeted SNES
print(list_of_consoles)
print()

#Dictionaries - A group of Key-Value Pairs. In a Dictionary, you access the values by first naming the key

empty_dict = {} #This is how you create an empty dictionary
empty_dict['Age'] = 18 #adding a key and value to an empty dictionary
empty_dict['Best N64 Game'] = "Legend of Zelda Ocarina of Time"
empty_dict['Fender'] = ["Telecaster", "Stratocaster", "Jazzmaster"]
print(empty_dict)
print(empty_dict['Fender']) #how to print a specific key
print(empty_dict["Fender"][0]) #This will print Telecaster
print(empty_dict["Fender"][1:3]) #This will print Stratocaster and Jazzmaster
remove_value = empty_dict.pop('Fender')
print(remove_value) #returns the value of all items in key for "Fender"
print(empty_dict) #As you see, this dictionary no longer has Fender list included as it was popped to a new variable
print()

new_person = {'name': "Chris", 'age':32, 'occupation': 'Full Stack Developer'}
new_person['name'] = 'Christopher'
print(new_person, "\n") #This is how you change a value in a defined key

#If you are ever unsure of a values datatype, use the "type" function to find out what it is
print(type(2.63))
print(type(new_person))

#For data types with length attributes, use "len" function to get the length

print(len(new_person))
print(len('Nintendo'))
print()

##Numbers/Integers - 3 basic types - floats, integers and complex

print(type(24))
print(type(3.9))
print(type(3j))
print()

##Random number generator -- Function is called "random" and must be imported
import random
print('This is my random # generator, the # will always be different')
print(random.randint(2,100))
print()

###Strings - Any Sequence of characters enclosed in "" or ''###

print("I love music - particulary blues, jazz, lo-fi\n")

#concatenating Strings and Variables with the print function
religion = "Buddhism"
print ("I am a fan of", religion,".")
print("I am a fan of " + religion + ".")
print(f"I am a fan of {religion}.")

#Type Casting or Explicit Type Conversion - changing a data type from one to another. For example, can't add a string and #
#print("hello" + 42) - this will throw an output error because you cannot add a string and an integer
print("hello " + str(42))

total = 35
user_val = "26"

#print(total + user_val) this wont work cause it is an integer and then a string. Let's fix this
print(total + int(user_val), "\n") # Here I used a comma instead of "+" to create a separate line


###f-strings - take a variable and add it into a string!
good_guy = "Link"
bad_guy = "Ganon"
date_of_duel = 10000

print(f"Our hero {good_guy.title()} fought a great duel against {bad_guy.title()}. It was fought {date_of_duel} years ago.\n")

###Built in String Methods - Most common are .title(), .upper(), .lower(). These are used when printing and only on strings

###List - A data type that allows us to hold a group of values###

ninjas = ["Rikimaru", "Jin Sakai", "Onikage", "Wolf from Sekiro"]
my_list = [4, 26, 5, "Link", "Zelda", True, False]
empty_list = []

##Add to an empty list
empty_list.append("New Item for the List - At line 175 in the code")
empty_list += ["put in here what you want to append"]
print(empty_list)

##You can concatenate Lists

fruits = ["apple", "orange", "strawberry"]
vegetables = ["carrots", "potato", "cucumber"]
print(fruits + vegetables, "\n")

###Dictionaries - A mutable set type with consists of key, value pairs

##Creating Dictionaries
weekend = {"Sun": "Sunday", "Sat": "Saturday"}
capitals = {}
capitals['Massachusetts'] = 'Boston'
capitals['Rhode Island'] = 'Providence'
capitals['New York'] = 'New York City - Manhattan'
print (capitals)

##Accessing Values in a Dictionary

print(weekend["Sun"])
print(capitals['Rhode Island'])

#Removing Values 
value_removed = capitals.pop('New York')
print(value_removed)
#OR
del capitals['Rhode Island']
print(capitals) #All that should print is [Massachusetts : Boston]
print()

##Nesting is allowed in Dictionaries
##Some built in Functions and Methods for Dictionaries
##Built In Functions
#len() - gives the length of the dictionary
#str() - produces a string representation of a dictionary
#type() - returns the type of passed variable

##Built In Methods
#.clear() - removes all elements from the dictionary 
#.copy() - returns a shallow copy dictionary
#items() - returns a list of dictionary's (key, value) tuple pairs
#.keys() - return a list of dictionary keys
#.values() - return a list of dictionary values

###Conditional Statements###

x = 12
if x > 50:
    print("bigger than 50")
else:
    print("smaller than 50")
    # because x is not greater than 50, the second print statement is the only one that will execute
    
    x = 55
if x > 10:
    print("bigger than 10")
elif x > 50:
    print("bigger than 50")
else:
    print("smaller than 10")
    # even though x is greater than 10 and 50, the first true statement is the only one that will execute, so we will only see 'bigger than 10'
    
if x < 10:
    print("smaller than 10")
    # nothing happens, because the statement is false

###Loops###

#A for loops can have 3 parts - initial value, top value, increment
for x in range(0,20+1,1):
    print(x, '\n')

for x in range(5,1,-3):
    print(x, '\n')

###########################################################################################################################
###For Loops Basic I

#1. Basic - Print all integers from 0 - 150
for numbers in range(0,150+1):
    print(numbers, '\n')
#2. Multiples of Five - Print all the multiples of 5 from 5 to 1000
for numbers in range(5,1000,5):
    print(numbers, '\n')
#3. Counting, the Dojo Way - Print the integers 1 to 100. If divisible by 5, print "coding" instead. If divisible by 10, print Coding Dojo
for numbers in range(0,101):
    if numbers % 10 == 0:
        print('coding dojo')
    elif numbers % 5 == 0:
        print('coding')
    else:
        print(numbers)
#4. Whoa. That Suckers Huge - Add odd integers from 0 to 500,000 and print the final sum
def hugesucker():
    sum = 0
    for numbers in range(0,500000):
        if numbers % 2 == 1:
            sum = sum + numbers
    print(sum, '\n')
hugesucker()

#5 Flexible Counter - Set 3 vars. lowNum, highNum and mult.

lowNum = 2
highNum = 9+1
mult = 3

for i in range(lowNum,highNum):
    if i % mult == 0:
        print (i)

print()

###########################################################################################################################

###Functions - A function is a named block of code that can execute and perform a specific task. It can be called and used as much as needed.

##To define a function, use "def". Below is an example of a simple function:

def add(a,b):
    x = a + b
    return(x)

print (add(5,5),"\n")

######Parameters and Arguments

def say_hi(name):
    print("Hi " + name)

say_hi("Chris")
say_hi("Lindsey")

######Returning Values - You have to include a return statement to obtain something done in your code block

def say_hi(name):
    return "Hi " + name

greeting = say_hi("Christopher")
print(greeting)

#####Debugging your code - Liberally use "print" statements to find out what your code is doing.

#####Functions Basic II

#1 Countdown - Create a function that accepts a number as an input. Return a new list that counts down by one, from the number 
# (as the 0th element) down to 0 (as the last element)

def countdown(num):
    for i in range(10, 0-1,-1):
        print (i)

print(countdown(10))

#2 Print and Return - Create a function that will receive a list with two numbers.
# Print the first value and return the second

def print_and_return(a,b):
    funcList = [a,b]
    for i in funcList:
        print(a)
        return(b)

print(print_and_return(5,10), "\n")


#3 First Plus Length - Create a function that accepts a list and returns the sum of the first value in the list 
#plus the lists length

def firstPlus(aList):
    for i in range(len(aList)):
        return (aList[0] + len(aList))
    
newList = [6,12,18]
print(firstPlus(newList), '\n')

#4 Values Greater Than Second - Write a function that accepts a list and creates a new list containing only the values from the original list that are greater than its
# second value. Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return false.


