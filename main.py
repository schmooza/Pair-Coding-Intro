import pandas as pd
from person01 import *
from person02 import *

print("Below is the data selected.\nTry selecting different data.\n")
outputp1 = loadDataPerson01()
# print (outputp1,"data selected by person 1")

outputp2 = loadDataPerson02()
# print (outputp2, "data selected by person 2")

finalOutput = pd.concat([outputp1, outputp2], axis=1)
#what is this?
# final = pd.concat[outputp1,outputp2]
print(finalOutput)

finalOutput.to_csv('outputData/outputfile_2sets.csv')

print("\n This program loads two sets of data and combines them into one file, check the outputData folder to see the result. ")
