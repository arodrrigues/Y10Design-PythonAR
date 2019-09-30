# Loops help us to do a particular task many times
# Example 1

# The range() function defaults to 0 as a starting value, however it is possible 
# to specify the starting value by adding a parameter: range(a, b, c) which means 
# values from 'a' to 'b' (but not including 'b') and increases by 3 each time

# lets add all of the numbers from 1 to 1000:

stars = ""
for x in range(10, 1, -1):
	stars = stars + "*"
	print(stars)
