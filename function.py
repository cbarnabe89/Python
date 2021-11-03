a = 5
b = 10

def add(a,b):
    x = a + b
    return x
print(add(a,b)) #this returns 15 for a value

#another example - here, variable a and b are passed through the function and a new value is returned in new_val variable

new_val = add(3,5)
print(new_val)

#another example - here a function is created - it prints a message and then we pass the arguments through the functions below

def say_hi(name):
    print("hi, " + name)

say_hi("Michael")
say_hi("Christopher")
say_hi("Eli")
print()

#returning values in functions

def say_hi(name):
    return "Hi " + name
greeting = say_hi("Michael")
print(greeting)

def nintendo(console):
    return "the best console is " + console
variable = nintendo("N64")
print(variable)

def add(a,b):
    x = a + b
    return x
sum1 = add(1,4)
sum2 = add(2,3)
sum3 = add(9,1)
sum4 = sum1 + sum2
print(sum4)
print(sum3)

#here is some independent practice to see if my output matches what I think it should be

def sandwich(bun, meat):
    lunch = bun + meat
    return lunch
meal1 = sandwich("white bread ", "ham")
print(meal1)

def date_time(date, time):
    let = date + time
    return let
appointment = date_time("may 26 ", "5:26")
print(appointment)
print()

def knight(sword, shield):
    weapons = sword + shield
    return weapons
warrior1 = knight("short sword ", "Hylian shield")
warrior2 = knight("katana ","no shield")
print(warrior1)
print(warrior2)

def arith(l,m):
    z = l / m 
    return z
prob1 = arith(100,50)
prob2 = arith(9,3)
prob3 = arith(50,25)
print(prob1,prob2,prob3)