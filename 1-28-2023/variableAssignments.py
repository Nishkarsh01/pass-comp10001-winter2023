#Variable Assignment

#Rules for variable names
#1. names can not start with a number
#2. names can not contain spaces, use _ intead
#3. names can not contain any of these symbols: '",<>/?|\!@#%^&*~-+
#4. it's considered best practice (PEP8) that names are lowercase with underscores
#5. avoid using Python built-in keywords like list and str
#6. avoid using the single characters l (lowercase letter el), O (uppercase letter oh) and I (uppercase letter eye) as they can be confused with 1 and 0

#Assigning Variables
#Variable assignment follows name = object, where a single equals sign = is an assignment operato

a=5

#Dynamic Typing
#Python uses dynamic typing, meaning you can reassign variables to different data types. This makes Python very flexible in assigning data types; it differs from other languages that are statically typed.

my_dogs = 2
my_dogs = ['Sammy', 'Frankie']
my_dogs = 2.3

#Determining variable type with type()
type(a)
type(my_dogs)
