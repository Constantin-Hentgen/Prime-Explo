def primeNeighbors(number):
	neighbors=[]
	for element in primeBank:
		if element > number:
			neighbors.append(primeBank[primeBank.index(element)-1])
			neighbors.append(element)
			break
	return neighbors

