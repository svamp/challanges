#!/usr/bin/python
# -*- coding: utf-8 -*-
"""

	Challange: Create a mastermind game, where the player enters 4 numbers and the computer tells the player how many
			   (but not wich) of the for numbers are correct.

	Source: http://usingpython.com/python-programming-challenges/

"""

import argparse, random, sys

def get_digits(dificulty):

	if dificulty == 'easy':
		print('Guess the 2 numbers')
		return str(random.randint(10,99))
	elif dificulty == 'normal':
		print('Guess the 3 numbers')
		return str(random.randint(100,999))
	elif dificulty == 'hard':
		print('Guess the 4 numbers')
		return str(random.randint(1000,9999))
	elif dificulty == 'expert':
		print('Guess the 5 numbers')
		return str(random.randint(10000,99999))


def scramble_list(orig):

	dest = orig[:]
	random.shuffle(dest)
	return dest


def game():

	parser = argparse.ArgumentParser(description='Guess the numbers in as few tries as possible. A (*) marks a correct number in the correct place. A (-) marks a correct number but in the wrong place. \n The order in witch the notations appear are randomized.')
	parser.add_argument('-l', '--limit', help='Limits tha amounts of guesses you can make before forfeiting the game', type=int, default=0)
	parser.add_argument('-d', '--dificulty', choices=['easy', 'normal', 'hard', 'expert'], default='normal', help='Defines how many numbers there are to be guessed')
	parser.add_argument('-c', '--cheat', help='If supplied shows the correct sollution',  action='store_true')
	parser.set_defaults(cheat=False)
	args = parser.parse_args()
	

	target = get_digits(args.dificulty)
	tries = 1
	limit = args.limit

	go_again  = ['Yes', 'Y', 'y', 'ye', 'Ye']
	quit = ['No', 'N', 'no', 'n']
	
	while True:

		if limit != 0 and tries >= limit:
			print('To bad.. The target was %s' % tries)

			while True:
				play_again = input('Do you want to play again? [Y/n]: ')
				if play_again in go_again:
					tries = 0
					target = get_digits()
					break
				elif play_again in quit:
					sys.exit(0)
				else:
					print('Please enter Yes or No')
					continue

		
		if args.cheat:
			print('Sollution: %s' % target)
		try:
			guess = input('{} > '.format(tries))
			if not guess.isdigit():
				raise ValueError('Thats not a number!\n')
		except ValueError as e:
			print(e)
			continue

		if len(guess) != len(target):
			print('Your guess does not match the number of numbers in the target number')
			continue

		if guess == target:
			print('Well done.. That took you %i attempts!' % tries)
			while True:
				play_again = input('Do you want to play again? [Y/n]: ')
				if play_again in go_again:
					tries = 1
					target = get_digits(args.dificulty)
					break
				elif play_again in quit:
					sys.exit(0)
				else:
					print('Please enter Yes or No')
					continue
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
		print(result)

		tries += 1


game()
