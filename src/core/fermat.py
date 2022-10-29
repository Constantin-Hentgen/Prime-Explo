import math, decimal
from core import inspector

# https://en.wikipedia.org/wiki/Fermat_number
def isFermat(number, primeBank):
	if inspector.isPrimeEnhanced(number, primeBank) and type(decimal.Decimal(str(math.log((math.log((number-1)**(1/math.log(2))))**(1/math.log(2))))).normalize()) == int:
		return True
	else:
		return False


# renvoie une quantité précise de nombre de Fermat
def getXfermat(quantity):
	fermatBank = []
	bound = 2
	while len(fermatBank) < quantity:
		fermatBank = getFermatUntil(bound)
		bound += 2	
	return fermatBank
