# Booleans

# True or False
#
# a = True
# b = False
#
# print(a == b) # False
# print (a != b) # True
# print (a >= True) # True
# print (b <= False) # True
#
# print( True and False) # False
# print(True or False) # True
#
# # Booleans are useful for quickly checking the state of something
# # The other area Booleans are really useful for are validating data types
#
# # Booleans with Data types
#
# hi = "Hello World!"
# print(hi.isalpha()) # False
# print(hi.islower()) # False
# print(hi.endswith("!")) # True
# print(hi.startswith("He")) # True
#
# x = 0
# y = 10
#
# print(bool(x)) # False - 0 is always false
# print(bool(y)) # True
# print(bool(z)) # True

# None

# None == Null in other languages

print(bool(None)) # False

x = None

print(x == False) # False
print(x == True ) #False

# Checking if variable is none

print(x == None) # direct comparison - more complex situation
print(x is None) # Best practice for checking if something is 'None'

print(type(x)) #  < class 'NoneType>