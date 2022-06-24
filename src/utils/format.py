import math

# renvoie un nombre sans les 0 inutiles en décimal
def dropZeros(number):
	decimalPart = number - math.floor(number)
	
	if decimalPart == 0:
		return math.floor(number)
	
	else:
		return number
