#!/usr/bin/env python3

import operator
import logging
import sys

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
#logger.setLevel(logging.INFO)
sh = logging.StreamHandler(sys.stdout)
logger.addHandler(sh)

def testFunc(arg1):
	temp = arg1 * arg1
	temp = arg1 * arg1
	temp = arg1 * arg1
	temp = arg1 * arg1
	temp = arg1 * arg1
	temp = arg1 * arg1
	temp = arg1 * arg1
	temp = arg1 * arg1
	temp = arg1 * arg1
	temp = arg1 * arg1
	temp = arg1 * arg1
	temp = arg1 * arg1
	return temp

def percent(arg1, arg2):
        temp = arg1 / 100
        temp = temp * arg2
        return arg1 + temp

def sum(arg):
	temp = 0;
	sys.stdout.write("\033[1;31m")
	sys.stdout.write("Sum of: ")
	sys.stdout.write("\033[0;0m")
	while len(arg) != 0:
		old_temp = temp
		temp += arg.pop()
		old_temp = temp - old_temp
		sys.stdout.write(str(old_temp))
		sys.stdout.write(" ")
	sys.stdout.write("\033[0;0m")
	print(" ")
	return temp

operators = {
	'+': operator.add,
	'-': operator.sub,
	'/': operator.truediv,
	'*': operator.mul,
	'%': percent,
	'^': operator.pow,
	'.': operator.ifloordiv,
}

def calculate(arg):
	stack = list()
	for token in arg.split():
		try:
			value = int(token)
			stack.append(value)
		except ValueError:
			if token == 'S':
				result = sum(stack)
				stack.clear()
				stack.append(result)
			elif token == 'C':
				sys.stdout.write("\033[0;32m")
				sys.stdout.write("Copy and push: ")
				sys.stdout.write("\033[0;0m")
				sys.stdout.write(str(stack[len(stack)-1]))
				sys.stdout.write(" ")
				print(" ")
				stack.append(stack[len(stack)-1])
			else :
				function = operators[token]
				arg2 = stack.pop()
				arg1 = stack.pop()
				sys.stdout.write("\033[1;34m")
				sys.stdout.write("Operator ")
				sys.stdout.write(token)
				sys.stdout.write(": ")
				sys.stdout.write("\033[0;0m")
				sys.stdout.write(str(arg1))
				sys.stdout.write(" ")
				sys.stdout.write(str(arg2))
				sys.stdout.write(" ")
				print(" ")
				result = function(arg1, arg2)
				stack.append(result)
		logger.debug(stack)

	if len(stack) != 1:
		raise TypeError

	return stack.pop()

def main():
	while True:
		print(calculate(input('rpn calc> ')))

if __name__ == '__main__':
	main()
