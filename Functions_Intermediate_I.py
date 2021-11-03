#1 Update Values in Dictionaries and Lists
#Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
#Change the last_name of the first student from 'Jordan' to 'Bryant'
#In the sports_directory, change 'Messi' to 'Andres'
#Change the value 20 in z to 30

x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

#1
x[1][0] = 15
students[0]['last_name'] = 'Bryant'
sports_directory['soccer'][0] = 'Andres'
z[0]['y'] = 30

print (x)
print (students)
print(sports_directory)
print(z)

#2 Iterate Through a List of Dictionaries
#Create a function iterateDictionary(some_list) that, given a list of dictionaries, the
#function loops through each dictionary in the list and prints each key and the
#associated value. For example, given the following list:

def iterateDictionary(students):
    for student in range(len(students)):
        print(students[student])

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
iterateDictionary(students) 
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
#first_name - Michael, last_name - Jordan
#first_name - John, last_name - Rosales
#first_name - Mark, last_name - Guillen
#first_name - KB, last_name - Tonel

#3. Get Values from a List of Dictionaries
#Create a function that given a list of dictionaries and a key name, 
#the function prints the value stored in that key for that dictionary.
#for example, iterateDictionary2('first_name', students)should output\

def iterateDictionary2(key_name, some_list):
    for name in some_list:
        print(name[key_name])

iterateDictionary2('first_name', students)
print()
iterateDictionary2('last_name', students)
print()

students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

#4. Iterate Through a Dictionary with List Values
#Create a function printInfo(some_dict) that given a dictionary whose values are all lists,
#prints the name of each key along with the size of its list, and then prints the associated
#values within each key's list. 

def printInfo(some_dict):
    print(str(len(some_dict['locations']))+" LOCATIONS")
    for location in some_dict["locations"]:
        print(location)
    print()
    print(str(len(some_dict['instructors'])) +" INSTRUCTORS")
    for instructor in some_dict["instructors"]:
        print(instructor)



dojo = {
'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
printInfo(dojo)

