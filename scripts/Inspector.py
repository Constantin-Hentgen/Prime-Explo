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

