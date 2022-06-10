
# renvoie tous les nombres premiers inférieurs à une borne
def primeFinderUntil(bound):
	for potentialPrime in range(primeBank[-1] + 1,bound):
		if isPrimeEnhanced(potentialPrime):
			primeBank.append(potentialPrime)


# renvoie tous les nombres premiers inférieurs à une borne
# @numba.jit
def primeFinderUntilEnhanced(bound):
	start = startTime()
	for potentialPrime in range(primeBank[-1] + 1,bound):
		if isPrimeEnhanced(potentialPrime):
			print(potentialPrime)
			primeBank.append(potentialPrime)
	return endTime(start, 2)



def primeFinderFromUntilEnhanced(boundInferior, boundSuperior):
	start = startTime()
	for potentialPrime in range(boundInferior,boundSuperior):
		if isPrimeEnhanced(potentialPrime):
			primeBank.append(potentialPrime)
	return endTime(start, 2)


# renvoie x nombres premiers
def xPrimeFinder(quantity):
	bound = 1
	while len(primeBank) < quantity:
		primeFinderUntil(bound)
		bound += 1


# renvoie le n-ième nombre premier
def getNthPrime(rank):
	xPrimeFinder(rank)
	return primeBank[-1]
