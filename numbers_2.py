# Using the range() function
for value in range (1,5):
	print (value)
# Starts counting at the first value and stops when reaches the second value

# Using range() to make a list of numbers
numbers = list(range(1,6))
print (numbers)

even_numbers = list(range(2,11,2))
print (even_numbers)
# 1st number = start number
# 2nd number = end value
# 3rd number = adding 2 repeatedly until it reaches or passes the end value
even_numbers = list(range(10,102,2))
print (even_numbers)

test_number = list(range(10,104,3))
print (test_number)

for value in range(10,50,3):
	print (value)

#squares
#1 empty list
#2 loop each value from 1 to 10 using the range function
#3 inside the loop, the value is raised to the second power and stored as varibale 'square'
#4 Values appended/added at the end of the list
squares = []
for value in range(1,11):
	square = value**2
	squares.append(square)

print (squares)
# 2 asterisks (**) = exponents
squares = []
for value in range(1,11):
	squares.append(value**2)
print (squares)

#List comprehension for square numbers

squares = [value**2 for value in range(1,11)]
print (squares)

# Simple statistics with a list of numbers
digits = [1,2,3,4,5,6,7,8,9,0]
print (min(digits))
print (max(digits))
print (sum(digits))

# Exercises
# 4-3. Counting to Twenty
for value in range (1,21):
	print (value)
# 4-4. One million
for value in range (1,1000001):
	print (value)
# 4-5. Summing a million
one_million = list(range(1,1000001))
print(min(one_million))
print(max(one_million))
print(sum(one_million))
# 4.6. Odd numbers
odd_numbers = list(range(1,20,2))
print (odd_numbers)
# 4.7. Threes
threes = list(range(3,31,3))
for number in threes:
	print (number)
# 4.8. Cubes

cubes = []
for value in range(1,11):
	cube = value**3
	cubes.append(cube)

for cube in cubes:
	print (cube)

# 4.9. Cube comprehension
cubes = [value**3 for value in range(1,11)]
# Prints value of each cube
for cube in cubes:
	print (cube)
# Prints a list
print (cubes)

