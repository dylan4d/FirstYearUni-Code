#Name: Dylan Forde
#Student ID: 120309116
#Programme: Data Science

def meanBoutsPerPatient ():
	filename = "InflammatoryIBS.csv"
	inFile = open(filename, 'r')
	denominator = 0
	patientId = 0

	for line in inFile:
		patient = line.split(',')
		numerator = 0
		for i in range(0,len(patient)):
			patient[i] = int(patient[i])
			numerator += patient[i]
		denominator = len(patient)

		avg_bouts_per_patient = numerator / denominator
		patientId += 1 
		print ("Patient", patientId, "had", round(avg_bouts_per_patient) , "inflammatory bouts on average")

	inFile.close()
		
def meanBoutsAcrossAllPatients ():
	filename = "InflammatoryIBS.csv"
	inFile = open(filename, 'r')
	numerator = 0
	denominator = 0
	for line in inFile:
		patient = line.split(',')
		for i in range(0,len(patient)):
			patient[i] = int(patient[i])
			numerator += patient[i]
		denominator += len(patient)

	avg_bouts_per_patients = numerator / denominator
	print ("The average number of inflammatory bouts on this trial medication is: ", round(avg_bouts_per_patients, 2))

	inFile.close()
		
meanBoutsPerPatient()
meanBoutsAcrossAllPatients()
