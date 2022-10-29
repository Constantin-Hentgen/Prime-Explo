from utils import inspector, time

# renvoie tous les nombres premiers inférieurs à une borne
def primeFinderUntil(bound, primeBank):
	for potentialPrime in range(primeBank[-1] + 1,bound):
		if inspector.isPrimeEnhanced(potentialPrime, primeBank):
			primeBank.append(potentialPrime)


# renvoie tous les nombres premiers inférieurs à une borne
def primeFinderUntilEnhanced(bound, primeBank):
	start = time.startTime()
	for potentialPrime in range(primeBank[-1] + 1,bound):
		if isPrimeEnhanced(potentialPrime):
			print(potentialPrime)
			primeBank.append(potentialPrime)
	return endTime(start, 2)


def primeFinderFromUntilEnhanced(boundInferior, boundSuperior, primeBank):
	start = time.startTime()
	for potentialPrime in range(boundInferior,boundSuperior):
		if inspector.isPrimeEnhanced(potentialPrime, primeBank):
			primeBank.append(potentialPrime)
	return time.endTime(start, 2)


# renvoie x nombres premiers
def xPrimeFinder(quantity,primeBank):
	bound = 1
	while len(primeBank) < quantity:
		primeFinderUntil(bound, primeBank)
		bound += 1


# renvoie le n-ième nombre premier
def getNthPrime(rank, primeBank):
	xPrimeFinder(rank, primeBank)
	return primeBank[-1]

