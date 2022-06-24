
import matplotlib.pyplot as plt

class Plot:
		
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
