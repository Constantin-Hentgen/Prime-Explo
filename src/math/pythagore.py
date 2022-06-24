# indique si le nombre entré est un nombre (X) de Pythagore : X = 4n + 1, n entier naturel
def isPythagorean(number):
	if isPrime(number):
		if type(dropZeros((number-1)/4)) == int:
			return True
		else:
			return False
	else:
		return False


# renvoie tous les nombres de Pythagore inférieurs à une borne
def getPythagoreanUntil(bound):
	pythagoreanBank = []
	for i in range(bound):
		if isPythagorean(i):
			pythagoreanBank.append(i)
	return pythagoreanBank


# renvoie une quantité finie de nombre de Pythagore
def getXpythagorean(quantity):
	pythagoreanBank = getPythagoreanUntil(quantity)
	bound = 5
	while len(pythagoreanBank) < quantity:
		pythagoreanBank = getPythagoreanUntil(quantity + bound)
		bound += 5
	return pythagoreanBank

