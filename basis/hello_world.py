#!/usr/bin/python3

# Hello world!
this_is_a_variable = "We like camel casing for some reason"
print(this_is_a_variable)

# Numbers
counter = 100  # integer
miles = 1000.0  # floating point (float)
name = "Jhon"  # string
# the standars are: numbers, strings, lists, tuples, dictionaries.

# delete references
del counter, miles, name

# numerical types: int, long, float, complex.

# Strings as arrays
test = "Hello word!"
h = test[0]
w = test[6]
hello = test[0:6]
print(hello)

# lists
list = ['something', 2, 'laskdjaslkdj', 1.3]
tinylist = [132, 'tommy']

print(list + tinylist)
print(list[0])
print(list[0:1])

# arrays []
# tuples () -> tuples are readonly arrays.
# dictionaries {}
dictio = {'name': 'tomi', 'age': 22}
print('Name ' + dictio.get('name') + ', ' +
      str(dictio.get('age')) + ' years old.')

a = 1
