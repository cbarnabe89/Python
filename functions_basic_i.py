#1
def number_of_food_groups():
    return 5
print(number_of_food_groups())
#the number 5

#2
def number_of_military_branches():
    return 5
#print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())
#this will throw an error because it is not a defined function

#3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())
#this will return 5 as once it is returned, the code stops executing

#4
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())
#this will print the integer 5 because the return terminates the function

#5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)
#this will print 5. Nothing is returned here so x will not have a value printed


#6
def add(b,c):
    print(b+c)
#print(add(1,2) + add(2,3))
#Output will be 3,5

#7
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))
#output will be 25 because the return statement defines the items as a string with no space between


#8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())
#it will print the result of output, which is 10 because if statement is false, so it goes to else

#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3)) # returns 7
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3)) # returns 14
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
#returns 7 + 14 = 21

#10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))
#returns the function "addition". Value returned is 8

#11
b = 500 #defines a variable b as the integer 500
print(b) #prints 500 here
def foobar(): #creates a function called foobar here with no parameter entered
    b = 300 #redefines the variable b as the integer 300 in the local 
    print(b) #prints the new variable of b as 300
print(b) #prints 500 - because this is the global variable
foobar() #prints nothing as this variable did not return a value
print(b) #prints 500 - because this is the global variable
#final output is 500, 500, 300, 500

#12
b = 500 #defines b as 500
print(b) #prints the integer 500
def foobar(): #creates a function called foobar 
    b = 300 #in the function sets a variable called b at 300
    print(b) #prints the integer 300
    return b #returns the variable b @ 300
print(b) #prints 500
foobar() #prints 300
print(b) #prints 500


#13
b = 500 #defines variable b at 500
print(b) #prints the integer 500
def foobar(): #defines a function called foobar with no parameter
    b = 300 #locally defines a variable called b @ 300
    print(b) #prints 300
    return b #returns value of b which is 300
print(b) #prints 500
b=foobar() #prints 300
print(b) #prints 300


#14
def foo(): #defines a variable called foo
    print(1) #prints 1
    bar() #prints nothing yet
    print(2) #prints 2
def bar(): #creates the function bar
    print(3) #will print 3 where bar is called
foo() #calls function


#15
def foo(): #defines a function called foo
    print(1) #prints the integer 1
    x = bar() #creates a variable called x with a value of the function bar
    print(x) #prints 3
    return 10 #not sure how this affects it
def bar(): #creates a function called bar
    print(3) #print 3
    return 5
y = foo()
print(y) #prints 1,3