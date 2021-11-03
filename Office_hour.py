#Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big"
#Example: biggie_size([-1,3,5,-5]) returns that same list, but whose values are now [-1,"big","big",-5]

##Pseudo code
# Write a function that has a list as parameter
# Create a For Loop to iterate through all numbers of the list
# Create If Statement to check if the number is positive or negative
# If the number is positive - change value to "big"
# return back that list

def biggie_size(listy):
    for i in range(len(listy)):
        if listy[i] > 0:
            listy[i] = 'big'
    print(listy)
    return listy


arr = [-1,2,3,-8]
biggie_size(arr)

#given a list of numbers, create a function to replace the last value with the number of positive values.
#example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it.
#example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it

#pseudo code
#Create a function that takes in a list
#create a for loop to iterate through the list
#create an if check to see if it is positive or negative
#if positive, add to pos_sum of positive variable
#replace the last value in list with pos_sum variable

def count_positives(listy):
    pos_sum = 0
    for i in range(len(listy)):
        if listy[i] > 0:
            pos_sum += 1
    listy[-1] = pos_sum
    print(listy)
    return listy
    
lit = [1,0,2,-9,-8,-5]
count_positives(lit)

#Maximum and Minimum problem - in Excel sheet

def min_max(listy):
    if len(listy) == 0:
        return False
    min = listy[0]
    max = listy[0]
    for i in range(1, len(listy)):
        if listy[i] < min:
            min = listy[i]
        elif listy[i] > max:
            max = listy[i]
    return f"The min: {min} | The max: {max}"

lit = [-1,0,-8,38]
print(min_max(lit))

