# find a way to make it automatic to check for each functions possible

def inspector(number):
	if isPrimeEnhanced(number):
		print("Prime !")
	else:
		if isMersenne(number):
			print("nombre de Mersenne")
		if isFermat(number):
			print("nombre de Fermat")
		if isPythagorean(number):
			print("nombre de Pythagore")
		if isSophieGermain(number):
			print("nombre de Sophie Germain")
		else:
			print("nombre parfaitement inintéressant")
			print(multiplesFinder(number))
			print("les nombres premiers voisins sont : ", primeNeighbors(number))


# tester la primalité uniquement depuis des nombres premiers jusqu'à *ceil(math.sqrt(number))
def isPrimeEnhanced(potentialPrime, primeBank):
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