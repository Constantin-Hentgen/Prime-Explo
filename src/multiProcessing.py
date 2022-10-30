from multiprocessing import cpu_count
from pathos.multiprocessing import ProcessingPool as Pool
from core import finder
import numpy as numpy
import time

# mode auto which detect the number of threads and split the tasks
# mode full custom where you choose the number of threads

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


primeBank = [2,3,5,7]
bound_A = 10
bound_B = 1000000

def parLaPuissanceDesCoeursProco(bound_A, bound_B):
	enonce = split(bound_A, bound_B)
	ultimae = numpy.concatenate(asynchronax(enonce[0], enonce[1], enonce[2], enonce[3]))
	# print(ultimae)
	return ultimae

# BENCHMARK

start = time.time()
finder.primeFinderFromUntilEnhanced(bound_A, bound_B, primeBank)
end = time.time()
print('standard : {}'.format(end-start))

start = time.time()
parLaPuissanceDesCoeursProco(bound_A, bound_B)
end = time.time()
print('multiprocessing : {}'.format(end-start))
