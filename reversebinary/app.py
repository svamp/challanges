#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
	
	Challange: Input any integer between 1 and 1 000 000 000 and convert it to binary.
			   Once converted flip the binary and convert it back to an integer.
			   Display the result.
    Sample:
	   Input 1: 12   -> Output 1: 3
	   Input 2: 1578 -> Output: 675

"""
import sys

def reverse_binary():
	""" 
		Prompts the user for an integer. Converts the integer to binary and reverses the binary before 
		converting it back to an integer and displays the result to the user.
	"""

	print('Please enter an integer between 1 and 1 000 000 000.')

	while True:
		try:
			integer = int(input('>> '))

			if 1 <= integer <= 1000000000:
				binary = bin(integer)[2::]
				reversed_binary = binary[::-1]
				result = int(reversed_binary, 2)
				print('The reverses binary number of %s is %s' % (integer, result))

			else:
				print('The number is not in the valid range. Please enter a number between 1 and 1 000 000 000')

		except ValueError:
			print('Thats not a number! Please enter an integer between 1 and 1 000 000 000')
			continue

reverse_binary()
