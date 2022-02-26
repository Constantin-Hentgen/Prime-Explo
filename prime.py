# Python program to check whether the given integer is a prime number or not
import time
import matplotlib.pyplot as plt
import numpy as np

primeBank = [2]
valueList = []
timeList = []

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


def primeFinderUntil(bound):
	for potentialPrime in range(primeBank[-1] + 1,bound):
		if isPrime(potentialPrime):
			primeBank.append(potentialPrime)


def xPrimeFinder(quantity):
	bound = 1
	while len(primeBank) < quantity:
		primeFinderUntil(bound)
		bound += 1


# start = time.time()
# primeFinderUntil(100)
# xPrimeFinder(100)
# runTime = (time.time() - start)
# print('\nTemps de calcul : ', round(runTime,3), ' sec')
# print(primeBank)


def getNthPrime(rank):
	xPrimeFinder(rank)
	return primeBank[-1]


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
# fonction pour avoil le nombre de calcul pour un temps

def timeFromSeconds(seconds):
  seconds = seconds % (24 * 3600)
  hour = seconds // 3600
  seconds %= 3600
  minutes = seconds // 60
  seconds %= 60
    
  return "%d:%02d:%02d" %(hour, minutes, seconds)


def timeReal(seconds):
	day = seconds // (24 * 3600)
	seconds = seconds % (24 * 3600)
	hour = seconds // 3600
	seconds %= 3600
	minutes = seconds // 60
	seconds %= 60

	return "%02d days %02d hours %02d min %02d sec" %(day, hour, minutes, seconds)


def getRawTime(quantity):
	if quantity >= 1500:
		return 25*(10**(-7))*(quantity**2) - 0.0075*quantity + 6


def predictTimeToCompute(quantity):
	return timeReal(getRawTime(quantity))

# intégrer Taylor Young pour trouver une meilleure fonction pour approximer

# EXEC

# plotTimeToCompute(10000)
# print(getNthPrime(6282))

# xPrimeFinder(20)
# print(primeBank)

# print(timeReal(3600*24))

print(predictTimeToCompute(82000000))