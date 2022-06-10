
def startTime():
	return time.time()


def endTime(start, accuracy):
	print(round(Decimal(time.time() - start),accuracy))
	return round(Decimal(time.time() - start),accuracy)


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


# fonction pour avoir le temps pour un nombre de calcul
def timeFromSeconds(seconds):
  seconds = seconds % (24 * 3600)
  hour = seconds // 3600
  seconds %= 3600
  minutes = seconds // 60
  seconds %= 60
    
  return "%d:%02d:%02d" %(hour, minutes, seconds)
