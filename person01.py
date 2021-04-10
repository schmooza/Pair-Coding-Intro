import pandas as pd

# this def loads the data from data-set.csv
def loadDataPerson01():
	data = pd.read_csv("data-set.csv",index_col=False) 
	
	# head prints the top 5 lines of the data.
	# print (data.head())
	
	# this code runs the def selectDataPerson01. it sends data to it.

	outputp1, outputp11 = selectDataPerson01(data)
	return outputp1, outputp11

# this code selects a column from the loaded data.AssertionError

def selectDataPerson01(data):
	# print(data["Female Count"])
	p1 = data["Female Count"]
	p11 = data["Asian Count"]
	p1
	return p1, p11

