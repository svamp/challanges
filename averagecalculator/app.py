#!/usr/bin/python
# -*- coding: utf-8 -*-

import argparse, statistics


def main():

	parser = argparse.ArgumentParser(description='Supply the program with a string of numbers. Either on at a time or comma seperated. Type \'calc\' to calculate avrages.')
	args = parser.parse_args()

	greeting()
	numbers_list = list()

	while True:

		string = input('>> ')

		if string.isdigit():
			numbers_list.append(float(string))
		elif ',' in string:
			for i in string.strip(' ').split(','):
				if i.isdigit():
					numbers_list.append(float(i))
				else:
					print('It looks like %s is not a number') % i
					continue
		elif string == 'calc':
			print('Mean average: %r') % statistics.mean(numbers_list)
			print('Median average: %r') % statistics.median(numbers_list)
			try:
				print('Mode: %r') % statistics.mode(numbers_list)
			except StatisticsError:
				print('Mode: No mode could be found')
		else:
			print('No valid input..')
			continue

main()

