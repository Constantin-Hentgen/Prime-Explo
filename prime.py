import time
import matplotlib.pyplot as plt
import math

primeBank = [2]
valueList = []
timeList = []

# renvoie si l'entrée est un nombre premier
def isPrime(potentialPrime):
	primeControl = []
	if potentialPrime in primeBank:
		return True
	for primeNumber in primeBank:
		if potentialPrime%primeNumber != 0:
			primeControl.append(True)
			if primeControl.count(True) == len(primeBank):
				return True
		else:
			return False


# renvoie un nombre sans les 0 inutiles en décimal
def dropZeros(number):
	decimalPart = number - math.floor(number)
	
	if decimalPart == 0:
		return math.floor(number)
	
	else:
		return number


# faire un latex avec le cheminement pour obtenir la formule
# renvoie si le nombre premier est un nombre de Mersenne
def isMersenne(number):
	if isPrime(number):
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
		if isPrime(i) and isMersenne(i):
			MersenneBank.append(i)
			MersennePowerBank.append(getMersennePower(i))
	
	return MersenneBank, MersennePowerBank


# renvoie tous les nombres premiers inférieurs à une borne
def primeFinderUntil(bound):
	for potentialPrime in range(primeBank[-1] + 1,bound):
		if isPrime(potentialPrime):
			primeBank.append(potentialPrime)


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


# trace le temps nécessaire pour une quantité de calcul
def plotTimeToCompute(quantity):
	start = time.time()
	bound = 1

	while len(primeBank) < quantity:
		bound += 1

		if len(primeBank)%50 == 0:
			valueList.append(len(primeBank))
			runTime = round((time.time() - start),3)
			timeList.append(runTime)

	fig, ax = plt.subplots(num="Détermination de nombres premiers")
	ax.plot(valueList, timeList);
	ax.set_xlabel('nombre de calcul')
	ax.set_ylabel('temps de calcul en secondes')
	plt.title('Temps de calcul Nombres Premiers')
	plt.show()


# fonction pour avoir le temps pour un nombre de calcul
def timeFromSeconds(seconds):
  seconds = seconds % (24 * 3600)
  hour = seconds // 3600
  seconds %= 3600
  minutes = seconds // 60
  seconds %= 60
    
  return "%d:%02d:%02d" %(hour, minutes, seconds)


# renvoie le nombre de jours, heures, minutes et secondes à partir de secondes
def timeReal(seconds):
	day = seconds // (24 * 3600)
	seconds = seconds % (24 * 3600)
	hour = seconds // 3600
	seconds %= 3600
	minutes = seconds // 60
	seconds %= 60

	return "%02d days %02d hours %02d min %02d sec" %(day, hour, minutes, seconds)


#renvoie le temps de calcul à partir d'un nombre de calculs (sur base d'un polynôme)
def getRawTime(quantity):
	if quantity >= 1500:
		return 25*(10**(-7))*(quantity**2) - 0.0075*quantity + 6


# renvoie le temps estimé de calcul avec ma machine pour une quantité donnée de nombres premiers
def predictTimeToCompute(quantity):
	return timeReal(getRawTime(quantity))


# determine si le nombre est un nombre de Fermat
def isFermat(number):
	if isPrime(number):
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


# détermine si un nombre possède des jumeaux (N+2 || N-2, N nombre premier)
def hasTwin(number):
	if (isPrime(number)):
		if (number >= 3 and isPrime(number-2)) or isPrime(number+2):
			return True
		else:
			return False
	else:
		return False


# renvoie le ou les jumeaux s'ils existent
def twinFinder(number):
	twins = []
	if (hasTwin(number)):
		if (number >= 3 and isPrime(number-2)):
			twins.append(number-2)
		if (isPrime(number+2)):
			twins.append(number+2)
	return twins
			

# détermine si un nombre est un nombre (X) de Sophie Germain : X est premier ainsi que (2*X + 1)
def isSophieGermain(number):
	if isPrime(number):
		if isPrime(2*number+1):
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


# renvoie le nombre sûr : soit le nombre 2x+1 avec x nombre premier et 2x+1 premier
def getTrustworthy(number):
	if isSophieGermain(number):
		return 2*number+1


# renvoie la décomposition
def primeNumberDecomposition(number):
	multiples = []
	reste = number

	if isPrime(number) == False:

		counter = 0
		while isPrime(reste) == False:
			if reste % primeBank[counter] == 0:
				multiples.append(primeBank[counter])
				reste = reste / primeBank[counter]

			else:
				counter += 1

	bigOne = 1
	for element in multiples:
		bigOne *= element

	multiples.append(int(number/bigOne))

	assumption = multiples
	final = []
	while len(assumption) > 0:
		final.append((assumption[0],assumption.count(assumption[0])))

		for i in range(assumption.count(assumption[0])):
			assumption.remove(assumption[0])

	return final



def primeNumberSumDecomposition(number):
	primeFinderUntil(round(math.sqrt(number))+50)
	reste = number
	primeMultiples = []
	coefficient = []

	reste = number
	for element in primeBank:
		counter = 0

		while reste - (element ** counter) > 0:
			counter += 1

		primeMultiples.append(element)

		if counter > 1:
			coefficient.append(counter-1)
		else:
			for i in range(reste):
				coefficient.append(0)
				break

		reste -= primeMultiples[-1]**coefficient[-1]
		total = 0

		for i in range(len(coefficient)):
			total += primeMultiples[i]**coefficient[i]
	
	primeMultiplesFinal = []

	for i in range(len(coefficient)):
		primeMultiplesFinal.append(primeMultiples[i])

	return primeMultiplesFinal, coefficient


def inspector(number):
	if isPrime(number):
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


def multiplesFinder(number):
	multipleBank = []
	for element in primeBank:
		if number % element == 0:
			multipleBank.append(element)
	return multipleBank


def primeNeighbors(number):
	neighbors=[]
	for element in primeBank:
		if element > number:
			neighbors.append(primeBank[primeBank.index(element)-1])
			neighbors.append(element)
			break
	return neighbors
# ________________________________________________________________________


# EXEC

primeFinderUntil(10000)


# analyse tous les nombres de 400 à 800
for i in range(400,800):
	print("_____________________")
	print(i)
	inspector(i)




# renvoie la décomposition en somme de puissance entre 2 bornes
# for j in range(345,567):
# 	decompo = primeNumberSumDecomposition(j)
# 	total = 0
# 	for i in range(len(decompo[1])):
# 		total += decompo[0][i]**decompo[1][i]
# 	print(j, primeNumberSumDecomposition(j), total == j)



# renvoie toutes les décompositions en produit de tous les nombres jusqu'à 200
# for i in range(1,200):
# 	if isPrime(i) == False:
# 		decompo = primeNumberDecomposition(i)
# 		total = 1

# 		for element in decompo:
# 			total *= element[0]**element[1]
# 		print(i, primeNumberDecomposition(i), total == i)
	


# retourne la décomposition de produit d'un nombre en particulier
# print(12722, primeNumberDecomposition(12722))


# trouve tous les nombres premiers inférieurs à 10k
# primeFinderUntil(100000)
# print(primeBank)


# plotTimeToCompute(1000)
# print(getNthPrime(6282))


# renvoie le 1200th nombre premier
# print(getNthPrime(1200))


# trouve 20 nombres premiers
# xPrimeFinder(20)
# print(primeBank)


# affiche le graph
# print(predictTimeToCompute(10000))


# affiche tous les nombres de Mersenne inférieurs à 10k
# print(getMersenneUntil(10000))


# renvoie tous les nombres de Fermat inférieurs à une borne
# print(getFermatUntil(300))

# renvoie 4 nombres de fermats
# print(getXfermat(4))


# renvoie si oui ou non le nombre entré posséde au moins un jumeau
# print(7,hasTwin(7))
# print(5, twinFinder(5))


# renvoie tous les nombres de Sophie Germain inférieurs à une borne
# print(getSophieGermainUntil(1000))


# renvoie une liste avec un nombre précis de nombres de Sophie Germain
# print(getXsophieGermain(10))


# renvoie tous les nombres de Pythagore inférieurs à une borne
# print(getPythagoreanUntil(100))


# renvoie une quantité finie de nombres de Pythagore
# print(getXpythagorean(10))


# renvoie tous les nombres de Sophie Germain qui sont inférieurs à 100 ainsi que le nombre sûr associé
# for i in range(100):
# 	if (isSophieGermain(i)):
# 		print(i, getTrustworthy(i))