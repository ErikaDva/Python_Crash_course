# Tuple = an immutable list (cannot change)
# Defining a tuple (using parentheses instead of brackets like for lists)
dimensions = (200, 50)
print (dimensions[0])
print (dimensions[1])
# Looping thorugh all values in a tuple
for dimension in dimensions:
	print (dimension)
# Writing over a tuple (overwriting value)
print ("Original dimensions:")
for dimension in dimensions:
	print (dimension)
dimensions = (400, 100)
print ("Modified dimensions:")
for dimension in dimensions:
	print (dimension)

# Exercises
# 4-13. Buffet
foods = ('pizza', 'pasta', 'fries', 'potatoes', 'chicken')
print ("Restaurant offers:")
for food in foods:
	print ("- " + food.title())

foods = ('beef', 'fish', 'fries', 'potatoes', 'chicken')
print ("Current menu:")
for food in foods:
	print ("- " + food.title())
