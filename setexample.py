#set is unique data - cannot be duplicated...

#create set 

# to create set in python { }  use curly braces

std_id = {111, 112, 113}
print(std_id)

#add() - add new elemets to a set
std_id.add(114)


print(std_id)

#mix-ids
# mix_id = {'Jack', 111, 'John', 112, 'Amy', 113}
# print(type(mix_id))

check_empty = set() # to create an empty set

check_empty = { } # empty dic 


# print(type(check_empty))



#Example: Update()
#update() - update the set with items of other collection types.

fruits = {'Apple', 'Orange', 'Banana'}
colors = ('Red', 'Brown', 'Blue')


#using update () method
fruits.update(colors)

print(fruits)









