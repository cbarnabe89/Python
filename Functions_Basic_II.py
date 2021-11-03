#1 Countdown - Create a function that accepts a number as an input.
#Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element)

from typing import List


def function(x):             #define a function
    List = []                #create an empty list for our function to take the output
    for i in range(x,-1,-1): #create a for loop that will go through the variables
        List.append(i)       #append the values
    return List              #return the output that way it isn't lost
print (function(5))          #print the working function with an argument

#2 Print and Return - Create a function that will receive a list with two numbers.
#Print the first value and return the second

def function(x,y):           #create a function with 2 parameters
    List = [x,y]             #create a list for X and Y
    for var in List:         #create a for loop just to get the value in the List we created
        print(x)             #print the first value
        return(y)            #return the second value
print (function(5,4))        #print the function running some arguments through it

#3 First Plus Length - Create a function that accepts a list and returns the sum of the first value 
#in the list plus the list's length

def function(a):                 #create a function and pass a parameter
    ListAdded = (a[0]) + len(a)  #create a variable to hold action we want returned
    return ListAdded             #return the variable

print (function([2,5,4,5,8]))    #print our function. First variable is 2 and length is 5. Output should be 7

#4 Values Greater than Second - Write a function that accepts a list and creates a new list containing 
#only the values from the original list that are greater than its 2nd value.
#Print how many values this is and then return the new list. If the list has less than 2 elements,
#have the function return False

def function(List):                    #define a function and give a parameter
    newList = []                       #create a new list to hold new values that are over second list item
    secondinp = List[1]                #create a variable for the second list item
    for i in range(len(List)):         #create a for loop to run through the range of the OG list
        if (List[i] > secondinp):      #if list item is greater than our second list item....
            newList.append(List[i])    #append to our newList variable list
    if (len(newList) > 1):             #if the length of the new list is greater than 1
        return(newList)                #return newList 
    else:                              #else
        return("false")                #return string false
finalList = [2,5,4,3,10,7,15]          #our final list

print(f"These numbers are higher than {finalList[1]}", function(finalList))
print("These numbers are higher than {} " .format(finalList[1]), function(finalList))

#5 This Length, That Value - Write a function that accepts two integers as parameters:
#size and value. The function should create and return a list whose length is equal to the
#given size and whose values are all the given value.

def length_and_value(length,value):   #create a new function for length and value
    newList = []                      #create a new list to hold new values
    for i in range(0, length):        #create a for loop to loop through the number provided in length variable
        newList.append(value)         #append the number looped in length into a new list of the value given
    return(newList)                   #return the new list

print(length_and_value(6, 2))


