import time
import matplotlib.pyplot as plt
import numpy as np

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
		primeFinderUntil(bound)
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


def predictTimeToCompute(quantity):
	return timeReal(getRawTime(quantity))




# EXEC


# trouve tous les nombres premiers inférieurs à 10k
# primeFinderUntil(100000)
# print(primeBank)

# plotTimeToCompute(1000)
# print(getNthPrime(6282))


# trouve 20 nombres premiers
# xPrimeFinder(20)
# print(primeBank)


# affiche le graph
# print(predictTimeToCompute(10000))