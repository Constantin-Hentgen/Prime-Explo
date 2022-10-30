import mysql.connector
from multiprocessing import cpu_count
from pathos.multiprocessing import ProcessingPool as Pool
from core import finder
import numpy as numpy
import time


def split(inferiorBound, superiorBound):
	totalCpu = cpu_count()
	totalRange = superiorBound - inferiorBound

	smallRanges = list(reversed([int(totalRange/totalCpu) for i in range(1,totalCpu)]))
	smallRanges.append(totalRange-int(totalRange/totalCpu)*(totalCpu-1))

	startingBounds = []
	endingBounds = []

	for cpu in range(0,totalCpu):
		if cpu == 0 or cpu == totalCpu - 1:
			# print(inferiorBound + cpu * smallRanges[cpu], inferiorBound + (cpu + 1) * smallRanges[cpu])
			startingBounds.append(inferiorBound + cpu * smallRanges[cpu])
			endingBounds.append(inferiorBound + (cpu + 1) * smallRanges[cpu])
		else:
			# print(1 + inferiorBound + cpu * smallRanges[cpu], inferiorBound + (cpu + 1) * smallRanges[cpu])
			startingBounds.append(1 + inferiorBound + cpu * smallRanges[cpu])
			endingBounds.append(inferiorBound + (cpu + 1) * smallRanges[cpu])

	return totalCpu, startingBounds, endingBounds, [primeBank for i in range(0,totalCpu)]

#	remettre dans l’ordre les résultats
	# pourquoi pas mettre directement dans la base de données les résultats (un peu bullshit quand même)

def asynchronax(coreNumber, startingBounds, endingBounds, banks):
	with Pool(coreNumber) as p:
		result = p.map(finder.primeFinderFromUntilEnhanced, startingBounds, endingBounds, banks)
	return result

def parLaPuissanceDesCoeursProco(bound_A, bound_B):
	enonce = split(bound_A, bound_B)
	ultimae = numpy.concatenate(asynchronax(enonce[0], enonce[1], enonce[2], enonce[3]))
	# print(ultimae)
	return ultimae

if __name__ == "__main__":
	iteration = 1000
	calculationRange = 25000

	myDb = mysql.connector.connect(
		host = "localhost",
		user = "root",
		password = "root"
	)
	
	cursor = myDb.cursor()
	cursor.execute("USE prime_base;")

	totalContribution = 0

	for i in range(iteration):

		# récupérer tous les primes
		cursor.execute("SELECT * FROM prime_table;")
		fetched_bank = [tuple[0] for tuple in cursor]
		originalLength = len(fetched_bank)
		primeBank = fetched_bank
		lastPrime = fetched_bank[-1]

		bound_A = lastPrime + 1
		bound_B = lastPrime + calculationRange

		contribution = parLaPuissanceDesCoeursProco(bound_A, bound_B)
		totalContribution += len(contribution)
		for primeNumber in contribution:
			print(int(primeNumber))

		# finder.primeFinderFromUntilEnhanced(fetched_bank[-1]+1, fetched_bank[-1]+calculationRange, fetched_bank)

		# contribution = [prime for prime in fetched_bank if prime > lastPrime]

		# print(contribution)

		for primeNumber in contribution:
			cursor.execute("INSERT INTO prime_table VALUES ({});".format(primeNumber))
		myDb.commit()
	
	print('La contribution s’élève à {} nombres premiers, Merci :) [total: {} nombres premiers dans la BDD]'.format(totalContribution, originalLength + totalContribution))
