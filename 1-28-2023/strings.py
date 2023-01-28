#Strings
#Strings are used in Python to record text information, such as names. Strings in Python are actually a sequence, which basically means Python keeps track of every element in the string as a sequence. For example, Python understands the string "hello' to be a sequence of letters in a specific order. This means we will be able to use indexing to grab particular letters (like the first letter, or the last letter).

#This idea of a sequence is an important one in Python and we will touch upon it later on in the future.

# We'll learn
#1.) Creating Strings
#2.) Asking user for input and Printing Strings
#3.) String Indexing and Slicing
#4.) String Properties
#5.) String Methods
#6.) Print Formatting

#Creating a String
#To create a string in Python you need to use either single quotes or double quotes. For example

a= "Hello World"
a= 'This is also a string'

#Be careful with quotes!
#The example below will result in an error
#a=' I'm using single quotes, but this will create an error'

#Printing a string
#We can use a print statement to print a string.

print('Hello World 1')
print('Hello World 2')
print('Use \n to print a new line')
print('\n')
print('See what I mean?')

# String Indexing
# We know strings are a sequence, which means Python can use indexes to call parts of the sequence. Let's learn how this works.

# In Python, we use brackets [] after an object to call its index. We should also note that indexing starts at 0 for Python. Let's create a new object called s and then walk through a few examples of indexing.

# Assign s as a string
s = 'Hello World'
# Print the object
print(s)
# Show first element (in this case a letter)
s[0]
s[1]
# Grab everything past the first term all the way to the length of s which is len(s)
s[1:]
# Grab everything UP TO the 3rd index
s[:3]
#Everything
s[:]
# Last letter (one index behind 0 so it loops back around)
s[-1]
# Grab everything but the last letter
s[:-1]
# Grab everything, but go in steps size of 1
s[::1]
# Grab everything, but go in step sizes of 2
s[::2]

#String Properties
#It's important to note that strings have an important property known as immutability. This means that once a string is created, the elements within it can not be changed or replaced. For example:

#Below statement gives us an error
#s[0] = 'x'

#Something we can do is concatenate strings!
# Concatenate strings!
# We can reassign s completely though!
s = s + ' concatenate me!'
print(s)

#We can use the multiplication symbol to create repetition!
letter = 'z'
print(letter*10)

#Basic Built-in String methods
#Objects in Python usually have built-in methods. These methods are functions inside the object (we will learn about these in much more depth later) that can perform actions or commands on the object itself.

#We call methods with a period and then the method name. Methods are in the form:

#object.method(parameters)

#Where parameters are extra arguments we can pass into the method. Don't worry if the details don't make 100% sense right now. Later on we will be creating our own objects and functions!

# Upper Case a string
s.upper()

# Lower case
s.lower()

# Split a string by blank space (this is the default)
s.split()

# Split by a specific element (doesn't include the element that was split on)
s.split('W')