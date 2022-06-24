from utils import Finder

if __name__ == "__main__":
	print("test d'existence")
	primeBank = [2]
	# Finder.primeFinderUntil(30, primeBank)
	Finder.primeFinderFromUntilEnhanced(30,primeBank)
	print(primeBank)


	# EXEC

	# bound = 100000

	# start = startTime()
	# primeFinderUntilEnhanced(bound)
	# oldtime = endTime(start, 6)

	# print("____________________")

	# start = startTime()
	# primeFinderUntil(bound)
	# newtime = endTime(start, 6)

	# print("____________________")

	# print("delta :", abs(oldtime-newtime))
	# print("ratio :", round(100*oldtime/newtime,1), "%  || ", round(100*newtime/oldtime,1), "%")



	# primeFinderUntilEnhanced(800)
	# # analyse tous les nombres de 400 à 800
	# for i in range(400,800):
	# 	print("_____________________")
	# 	print(i)
	# 	inspector(i)




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
	# primeFinderUntilen(100000)
	# print(primeBank)



	# primeBank = [2]
	# primeFinderUntil(100)
	# print(primeBank)
	# primeBank = [2]
	# primeFinderUntilEnhanced(100)
	# print(primeBank)

	# for element in primeBank:
	# 	print(element, isPrimeEnhanced(element))

	# print(getNthPrime(6282))

	# primeFinderUntilEnhanced(200000)


	# primeFinderFromUntilEnhanced(2, 240000)
	# print("___________________________________________________")
	# print(primeBank)
	# print(cpu_count())



	# 2,3,4,5,6

	# if __name__ == "__main__":
	# 	split()


	# print(len(primeBank))


	# écrit dans un document toute la liste 
	# f = open("bank", "w")
	# f.write(str(primeBank))
	# f.close()

	# faire une fonction qui va continuer à calculer des nombres premiers


	# renvoie le 798th nombre premier
	# print(getNthPrime(798))


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