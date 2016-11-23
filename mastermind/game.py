#!/usr/bin/python
# -*- coding: utf-8 -*-
"""

	Challange: Create a mastermind game, where the player enters 4 numbers and the computer tells the player how many
			   (but not wich) of the for numbers are correct.

	Source: http://usingpython.com/python-programming-challenges/

"""

import argparse, random, sys

def get_digits():

	return str(random.randint(1000,9999))

def greeting():

	print '\n\n\n######################## MASTERMIND ########################'
	print '#                                                          #'
	print '#  Guess the 4 numbers in as few tries as possible.        #'
	print '#                                                          #'
	print '#  A (*) marks a correct number in the correct place.      #'
	print '#  A (-) marks a correct number but in the wrong place.    #'
	print '#                                                          #'
	print '#  The order in witch the notations appear are randomized. #'
	print '#                                                          #'
	print '############################################################\n\n\n'


def scramble_list(orig):

	dest = orig[:]
	random.shuffle(dest)
	return dest


def game():

	greeting()

	target = get_digits()
	tries = 0
	go_again  = ['Yes', 'Y', 'y', 'ye', 'Ye']
	quit = ['No', 'N', 'no', 'n']
	
	while True:

		tries += 1

		try:
			guess = raw_input('{} > '.format(tries))
			if not guess.isdigit():
				raise ValueError('Thats not a number!\n')
		except ValueError as e:
			print e
			continue

		if guess == target:
			print 'Well done.. That took you %i attempts!' % tries
			while True:
				play_again = raw_input('Do you want to play again? [Y/n]: ')
				if play_again in go_again:
					tries = 0
					target = get_digits()
					print 'hello'
					break
				elif play_again in quit:
					sys.exit(0)
				else:
					print 'Please enter Yes or No'
					continue


		guess_list = list(guess)
		target_list = list(target)
		result_list = list()

		for idx, val in enumerate(guess_list):
			if val in target:
				if val == target[idx]:
					result_list.append('*')
				else:
					result_list.append('-')

		result = ''.join(scramble_list(result_list))
		print result


# Optional arguments

parser = argparse.ArgumentParser()
parser.parse_args()

game()
