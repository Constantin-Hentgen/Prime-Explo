import mysql.connector

from core import finder

if __name__ == "__main__":
	for i in range(50):
		myDb = mysql.connector.connect(
			host = "localhost",
			user = "root",
			password = "root"
		)
		
		cursor = myDb.cursor()
		cursor.execute("USE prime_base;")


		# récupérer tous les primes
		cursor.execute("SELECT * FROM prime_table;")
		fetched_bank = [tuple[0] for tuple in cursor]
		# print(fetched_bank[-1])
		lastPrime = fetched_bank[-1]

		# soit calculer de nouveaux primes soit fill les champs manquants (en partant des valeurs inférieurs) pour les primes existants
		finder.primeFinderFromUntilEnhanced(fetched_bank[-1]+1, fetched_bank[-1]+5000, fetched_bank)
		contribution = [prime for prime in fetched_bank if prime > lastPrime]

		print(lastPrime,contribution)

		for primeNumber in contribution:
			cursor.execute("INSERT INTO prime_table VALUES ({});".format(primeNumber))
		myDb.commit()
