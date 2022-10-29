# détermine si un nombre est un nombre (X) de Sophie Germain : X est premier ainsi que (2*X + 1)
def isSophieGermain(number):
	if isPrimeEnhanced(number):
		if isPrimeEnhanced(2*number+1):
			return True
		else:
			return False
	else:
		return False


# renvoie tous les nombres de Sophie Germain inférieurs à une borne
def getSophieGermainUntil(bound):
	sophieGermainBank = []
	for i in range(bound):
		if isSophieGermain(i):
			sophieGermainBank.append(i)
	return sophieGermainBank


# renvoie une quantité définie de nombre de Sophie Germain
def getXsophieGermain(quantity):
	sophieGermainBank = []
	bound = 1
	while len(sophieGermainBank) < quantity:
		sophieGermainBank = getSophieGermainUntil(bound)
		bound += 1
	return sophieGermainBank
