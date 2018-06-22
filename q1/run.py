#!/usr/bin/env python3


import random


# Helper function that gets the number of zeroes in the given list.
def get_num_zeroes(x):
	num = 0
	for i in x:
		if i == 0:
			num += 1
	return num

# Moves all the 0s in the list to the end while maintaining the order of the non-zero elements.
def move_zeroes(x):
	length = len(x)			# Length of the given list.
	num_zeroes = get_num_zeroes(x) 	# Gets the number of zeroes that must be moved.
	count = 0 			# Counts the number of zeroes that have been moved to the end of the list.
	i = length - 1 			# current index i is initially set to the last element's index.
	# Iterating through the list backward.
	while i >= 0:
		# If the current element is 0 and it is not in the correct place (at end of list).
		if x[i] == 0 and i <= length - num_zeroes:
			# Swap adjacent elements until the current element (0) is at end of list.
			while i < length - 1:
				temp = x[i]
				x[i] = x[i + 1]
				x[i + 1] = temp
				i += 1
				# If the current index is at the last element's index,
				# we successfully moved the 0.
				if i == length - 1:
					count += 1
		i -= 1
		# If we have moved all zeroes to the end of the list we're done, break out of the loop.
		if count == num_zeroes:
			break
	return x # Returns the same list that was passed in as an argument (#in-place).

# My alternate implementation of the function using list comprehensions (not in-place).
#def move_zeroes(x):
#	return [not_zero for not_zero in x if not_zero != 0] + [zero for zero in x if zero == 0]

# Tests
if __name__ == "__main__":
	# Given test case.
	x = [0, 0, 1, 0, 3, 12]
	print("Given list:")
	print(x)
	print("Result:")
	print(move_zeroes(x))
	print()
	# Random test case.
	lst = [0, 0] # Loads two zeroes into the list for simpler testing.
	for i in range(9): # Loads eight more random integers into the list.
		rand_num = random.randint(0, 25)
		lst.append(rand_num)
	print("Given list:")
	print(lst)
	print("Result:")
	print(move_zeroes(lst))
