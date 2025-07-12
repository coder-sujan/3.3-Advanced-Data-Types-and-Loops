#dictionary collection of items, - similar to list and tuple.

#key-value pair 

# country code  key  || phone number - value - key value pair 


# create dictionary - using { } - curly braces

#country and thier capitals
country_caps = {
    "Germany" : "Berlin", 
    "England" : "London",
} 

print(country_caps)


print(country_caps['Germany']) # access the items from dict


#del keyword
del country_caps["Germany"] # remove specific items

#clear() to remove everything
country_caps.clear()

print(country_caps)

