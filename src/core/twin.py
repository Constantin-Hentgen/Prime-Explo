# détermine si un nombre possède des jumeaux (N+2 || N-2, N nombre premier)
def hasTwin(number):
	if (isPrimeEnhanced(number)):
		if (number >= 3 and isPrimeEnhanced(number-2)) or isPrimeEnhanced(number+2):
			return True
		else:
			return False
	else:
		return False


# renvoie le ou les jumeaux s'ils existent
def twinFinder(number):
	twins = []
	if (hasTwin(number)):
		if (number >= 3 and isPrimeEnhanced(number-2)):
			twins.append(number-2)
		if (isPrimeEnhanced(number+2)):
			twins.append(number+2)
	return twins
