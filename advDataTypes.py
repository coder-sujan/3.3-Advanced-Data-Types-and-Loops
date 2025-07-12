#introducing List

# [] list created by using square brackets

# items are seperated by commas.

std_ages = [20,25,29] #3 items in the list

# print(std_ages)



#now with diff data types
#USING ONLY 1 STUDENT DETAILS   

std_ages_and_names = ['jack', 20, 'PYTHON', ['completed projects: ', 10] ] #3 items in the list

# print(std_ages_and_names)

#characteristics of list

#list are ordered
#list are mutable
#also allows duplicates




# Accessing the list....
#positive index starts from 0 - first element 
#negative index starts from -1 - last elemnet
languages = ['Python', 'Java', 'C++']

# print(languages[-1])



#Example: Add Elemnet to a list

#our list of fruits ver 1
fruits = ['apple', 'orange', 'banana']
# print('Fruit List V1.0: ', fruits)


#adding new fruit to a list uisng keyword  " .append "
fruits.append('cherry')

#our list of fruits ver 1.1
# print('Fruit List V1.1: ', fruits)



#Example: Add Elements at specific Index

#our list of fruits ver 1
fruits = ['apple', 'orange', 'banana']
# print('Fruit List V1.0: ', fruits)


#adding new fruit to a specific index of a list uisng keyword  " .insert "
fruits.insert(0,'cherry') #define our index number and list items

#our list of fruits ver 1.1
# print('Fruit List V1.1: ', fruits)



#Example: extend() - to join or combine 2 diff lists/multiple list

numbers = [1,2,3,4]

# print('1st List of Numbers: ', numbers)

other_numbers = [5,6,7,8]
# print('2nd List of Numbers: ', other_numbers)


#adding elements of one list to another
numbers.extend(other_numbers)


#print the two diff list together...
# print('Total List of Numbers: ', numbers)




#Example: Update / Change / Edit the list items

colors = ['Red', 'Black', 'Blue', 'orange']

# print('List of Colors: ', colors)


#edit / change/ replace/ update  the items of list
#replacing the index 0 and 1 color 'Red' to 'Green' and 'Black' to 'Purple'
colors[0] = 'Green'
colors[1] = 'Purple'

# print('Updated Colors List: ', colors)

del colors[1]

print('Removed Colors List: ', colors)

#Example of Removing list items

numbers_of_list = [1,2,3,4]

numbers_of_list.remove(2)

print('Removed Colors List: ', numbers_of_list)

#Access and remove list of items 

# del variabl_name[0] along with index number 


#Example: Python List Length

names = ['jack', 'Amy', 'John']

print('Total Elements: ', len(names))










