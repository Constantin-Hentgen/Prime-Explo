def multiplesFinder(number):
	multipleBank = []
	for element in primeBank:
		if number % element == 0:
			multipleBank.append(element)
		if element > number:
			break
	return multipleBank
