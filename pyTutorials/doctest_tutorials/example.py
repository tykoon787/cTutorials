def product(a: int, b: int):
	"""
	Returns the product of two numbers

		Parameters: 
				a (int): An integer number
				b (int): An integer number

		Returns: 
			Product of a and b

	>>> product(2,3)
	6
	>>> product(7,3)
	21
	>>> product('a',3)
	'aaa'
	"""
	return a * b

if __name__ == '__main__':
	import doctest
	doctest.testmod(verbose=True)
