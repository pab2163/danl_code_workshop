# short comments

'''
Long comments

All lines in here will be commented out


COMMENTS:
	In the script, not run as code
	Explain what the code is doing
	Notes on the code -- 'documentation'
'''


'''
A few notes about python code:
-Run from top to bottom

Running python code from the comand line

python <name of script>
'''


# ACTUAL PYTHON TIME #####

'''
4 primitive data types

String - 'words, letters, text data' (strings are always represented with quotes)
Integer - numeric data, whole numbers
Float - numerica, have decimals
Boolean - True vs. False (True == 1, False == 0)
'''


'''
ASSIGNING VARIABLE
'SAVING VARIABLES'

Single equals sign
Assignment goes right to left

Variables are BOXES:
-Box label: variable name
-Box contents: data stored in the variable
'''


# STRING
my_string = 'hello world!'

# print out the CONTENTS of my_string to cmd line
print(my_string)

# type() gives you what data type something is
print(type(my_string))

my_string2 = "happy friday!"

# add 2 strings?
my_string3 = my_string + my_string2

# print out the sum of the two strings
print(my_string3)


# Integers and floats (number data)
my_int = 3
print(my_int)
print(type(my_int))

my_float = 3.0
print(my_float)
print(type(my_float))


'''
Math in python

+ addition
- subract
* multiply
/ division

Python obeys order of operations (PEMDAS)
Parenthesis, exponents, multiplication, addition, subtraction
'''

print(2+2)
print(2-2)
print(2+6*3)
print((2+6)*3)

# doing math with variables
number_3 = my_int*my_float / 1000
print(number_3)

# updating a variable, including using it's current value
number_3 = number_3 + 3
print(number_3)


# BOOLEAN DATA

my_bool = True
my_bool2 = False

print(my_bool)
print(type(my_bool))

# why is this happening

print(my_bool + my_bool2)
print(my_bool*700)


# type conversion
print(my_int)
print(type(my_int))

# convert my_int to a string
my_new_string = str(my_int)
print(my_new_string)
print(type(my_new_string))


