#Name: Dylan Forde
#Student ID: 120309116
#Programme: Data Science

def meanBoutsPerPatient ():
    filename = "InflammatoryIBS.csv"
    inFile = open(filename, 'r')
    lst= [0]
    
    for line in inFile:
        patient = line.split(',')
        for i in range(0,len(patient)):
            patient[i] = int(patient[i])
        lst.append(sum(patient) / len(patient))
        meanPerPatient = [[lst.index(element), element] for element in lst[1:]]
    inFile.close()
    return meanPerPatient

def meanBoutsAcrossAllPatients ():
    filename = "InflammatoryIBS.csv"
    inFile = open(filename, 'r')
    lst= []
    for line in inFile:
        patient = line.split(',')
        for i in range(0,len(patient)):
            patient[i] = int(patient[i])
            lst.append(patient[i])
        average = sum(lst) / len(lst)
    
    print ("The average number of inflammatory bouts on this trial medication is: ", round(average, 2))
    
    inFile.close()


def writeToFile (boutList, filename):
    boutList = meanBoutsPerPatient()
    f = open(filename, "w")
    for bouts in boutList:
        L = ["Patient ", str(bouts[0]), " had ", str(bouts[1]), " inflammatory bouts on average", "\n"]

        f.writelines(L) 
    f.close()
meanBouts = meanBoutsPerPatient()
	

writeToFile(meanBouts, "meanBoutsPerPatient.txt")

meanBoutsAcrossAllPatients()