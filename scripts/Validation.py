
# tester la primalité uniquement depuis des nombres premiers jusqu'à *ceil(math.sqrt(number))
def isPrimeEnhanced(potentialPrime):
	primeControl = []
	if potentialPrime in primeBank:
		return True
	for primeNumber in primeBank:
		if potentialPrime % primeNumber == 0:
			return False
	return True


# renvoie si l'entrée est un nombre premier
# def isPrime(potentialPrime):
# 	primeControl = []
# 	if potentialPrime in primeBank:
# 		return True
# 	for primeNumber in primeBank:
# 		if potentialPrime%primeNumber != 0:
# 			primeControl.append(True)
# 			if primeControl.count(True) == len(primeBank):
# 				return True
# 		else:
# 			return False

