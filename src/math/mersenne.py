import math
# faire un latex avec le cheminement pour obtenir la formule
# renvoie si le nombre premier est un nombre de Mersenne
def isMersenne(number):
	if isPrimeEnhanced(number):
		if type(dropZeros(math.log((number+1)**(1/math.log(2))))) == int:
			return True
	else:
		return False


# renvoie la puissance de 2 d'un nombre premier de Mersenne
def getMersennePower(number):
	if isPrime(number):
		if isMersenne(number):
			return dropZeros(math.log((number+1)**(1/math.log(2))))


# renvoie la liste des nombres premiers de Mersenne inférieurs à une borne ainsi que leur puissance de 2
def getMersenneUntil(bound):
	MersenneBank = []
	MersennePowerBank = []

	for i in range(bound):
		if isPrimeEnhanced(i) and isMersenne(i):
			MersenneBank.append(i)
			MersennePowerBank.append(getMersennePower(i))
	
	return MersenneBank, MersennePowerBank

