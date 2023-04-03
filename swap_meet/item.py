# There is a module (file) named item.py inside of the swap_meet package 
# (folder)

# Inside this module, there is a class named Item
class Item:
    pass
  

# Each Item will have an attribute named id, which is a unique integer 
# by default

# There are many ways to generate numbers, but generating numbers 
# without duplicates takes some care. Happily, Python has a package 
# called uuid that can help!
# If we import the uuid package in item.py, with a little research 
# we can use one of the functions uuid provides to create large 
# unique numbers meant to be used as identifiers
# Specifically, you'll need to choose which of the uuid package's 
# functions to use, so be sure to consider which function will work best 
# for creating a unique integer
# Note that this package's functions return UUID objects, not integers 
# as such, but UUID objects have an attribute int which allow us to 
# access their value as an integer
# When we initialize an instance of Item, we can optionally pass in an 
# integer with the keyword argument id to manually set the Item's 
# id
