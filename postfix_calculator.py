# -*- coding: utf-8 -*-

from operator import add, mul, truediv, sub, neg, floordiv
from math import sin, pi, e
try:
    import readline
except ImportError:
    pass

FUNCTIONS = {
    'sin': (1, sin),
    '+': (2, add),
    '*': (2, mul),
    '/': (2, truediv),
    '//': (2, floordiv),
    '-': (2, sub),
    'neg': (1, neg),
    'pi': (0, lambda: pi),
    'del': (1, lambda a: None),
    'e': (0, lambda: e),
    'len': (None, lambda *args: tuple(args) + tuple((len(stack), ))),
    'cp': (1, lambda a: (a, a)),
    '**': (2, pow),
    'sum': (None, lambda *args: tuple(args) + tuple((sum(stack), ))),
    'swap': (2, lambda a, b: (b, a))
}

stack = []
result = None

def format_prompt():
	return ''.join((
		'..., ' if len(stack) > 3 else '[',
		', '.join(map(str, stack[-3:])),
		']',
		'({})'.format(len(stack)) if len(stack)> 3 else '',
		' >>> '
	))

while True:
    user_input = input(format_prompt())
    if user_input in FUNCTIONS:
        operands_count, operation = FUNCTIONS[user_input]
        if operands_count is None:
            operands_count = len(stack)
        
        if len(stack) >= operands_count:
            operands = stack[:-(operands_count + 1):-1]
            try:
                result = operation(*reversed(operands))
            except ArithmeticError as exception:
                print('Arithmetic error: {}.'.format(exception))
            else:
                stack = stack[0:len(stack)-operands_count]
                if hasattr(result, '__iter__'):
                    stack.extend(result)
                elif result is not None:
                    stack.append(result)
        else:
            print('Not enought items in stack this function.')
    elif user_input.isdigit():
        stack.append(int(user_input))
    elif '.' in user_input or ',' in user_input:
        stack.append(float(user_input.replace(',', '.')))
    elif user_input != "":
    	print('Unknown operation.')
        