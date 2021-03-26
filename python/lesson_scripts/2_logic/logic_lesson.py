'''
LOGICAL OPERATORS - always output True/False

= variable assignment (saving a variable)
== test of equality
'''

# Numeric logic (math comparisons)
print(2 == 2)
print(2 > 2)
print(2 >=2)

# integers and floats will be equal if values are the same
print(2.00000 == 2)

# string comparisons
print('2' == 2)
print('hi' == 'hello')

# case sensitive?
print('HI' == 'hi')


# ! means 'not'
print(2 != 2)

# booleans
print(True == 1)

a = 'True'

print(a == 'True')
print(a == True)

# can a string be greater than another string?
print('cat' >= 'bat')
print('bat' >= 'cat')


# COMPOUND LOGIC: or, and, not


# or -- return True if either one is true
print(2 == 3 or 2 < 3)

# and -- only return True if BOth are true
print(2 == 3 and 2 < 3)

# not
print(2 == 3 or not 2 == 2)



'''
Conditional statements - control code flow

TELLING PYTHON WHICH CODE TO RUN

if
else
elif

assert() -- check that something is true, crash script if not
'''

a = 2.7
if a > 3:
	# INSIDE
	# this code ONLY runs if the logical operator is True
	print('Its greater than 3, yay!') 
	
	# INSIDE
	print('hi earth')

# OUTSIDE (not conditional on anything)
print('hello world')

print('greetings planet')


# using elif & else to specify multiple conditions
b = -1
if b >= 5:
	print('hannah')
elif b >=3:
	print('sarah')
elif b >= 0:
	print('nick')
else:
	print('anshita')



# two if statements in a row?

c = 'chicken'

# nested if statements
if c == 'chickenB':
	print('chicken1')
if c == 'chicken':
	print('chicken2')


if c == 'chicken' and b > 0:
	print('chicken0')



# input validaation with logic

# participant_age = input('What is your age? ')

# if int(participant_age) < 150 and int(participant_age) > 0:
# 	print('valid age')
# else:
# 	print('invalid age, try again')


# FANCY Input Validation

while True:
	try:
		participant_age = input('What is your age? ')
		if int(participant_age) < 150 and int(participant_age) > 0:
			print('Thank you!')
			break
	except:
		print('invalid age response')