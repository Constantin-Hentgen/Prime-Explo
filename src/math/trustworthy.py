# renvoie le nombre sûr : soit le nombre 2x+1 avec x nombre premier et 2x+1 premier
def getTrustworthy(number):
	if isSophieGermain(number):
		return 2*number+1
