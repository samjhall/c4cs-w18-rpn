#!/usr/bin/env python3

import operator
import logging
import sys

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
#logger.setLevel(logging.INFO)
sh = logging.StreamHandler(sys.stdout)
logger.addHandler(sh)


def percent(arg1, arg2):
        temp = arg1 / 100
        temp = temp * arg2
        return arg1 + temp

def sum(arg):
	temp = 0;
	while len(arg) != 0:
		temp += arg.pop()
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
				stack.append(stack[len(stack)-1])
			else :
				function = operators[token]
				arg2 = stack.pop()
				arg1 = stack.pop()
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
