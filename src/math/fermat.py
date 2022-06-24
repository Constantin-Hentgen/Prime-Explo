import math

# determine si le nombre est un nombre de Fermat
def isFermat(number):
	if isPrimeEnhanced(number):
		if number > 2:
			if type(dropZeros(math.log((math.log((number-1)**(1/math.log(2))))**(1/math.log(2))))) == int:
				return True
			else:
				return False
		else: 
			return False
	else:
		return False


# renvoie tous les nombres de Fermat inférieurs à une borne
def getFermatUntil(bound):
	fermatBank = []
	for i in range(bound):
		if isFermat(i):
			fermatBank.append(i)
	return fermatBank


# renvoie une quantité précise de nombre de Fermat
def getXfermat(quantity):
	fermatBank = []
	bound = 2
	while len(fermatBank) < quantity:
		fermatBank = getFermatUntil(bound)
		bound += 2	
	return fermatBank
