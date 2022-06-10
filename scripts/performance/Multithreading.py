# 2 modes : auto which detect the number of threads and split the tasks
# mode full custom where you choose the number of threads

def split():
	primeFinderFromUntilEnhanced(2, 120000)
	a = Process(target=primeFinderFromUntilEnhanced, args=(120001,140000,))
	b = Process(target=primeFinderFromUntilEnhanced, args=(140001,160000,))
	c = Process(target=primeFinderFromUntilEnhanced, args=(160001,180000,))
	d = Process(target=primeFinderFromUntilEnhanced, args=(180001,200000,))
	e = Process(target=primeFinderFromUntilEnhanced, args=(200001,220000,))
	f = Process(target=primeFinderFromUntilEnhanced, args=(220001,240000,))
	
	a.start()
	b.start()
	c.start()
	d.start()
	e.start()
	f.start()

	a.join()
	b.join()
	c.join()
	d.join()
	e.join()
	f.join()