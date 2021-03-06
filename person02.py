import pandas as pd

# this def loads the data from data-set.csv
def loadDataPerson02():
	data = pd.read_csv("data-set.csv",index_col=False) 
	
	# head prints the top 5 lines of the data.
	# print (data.head())
	
	# this code runs the def selectDataPerson01. it sends data to it.

	outputp2, outputp22 = selectDataPerson02(data)
	return outputp2, outputp22

# this code selects a column from the loaded data.AssertionError

def selectDataPerson02(data):
	# print(data["Male Count"])
	p2 = data["Female Count"]
	p22 = data["Black or African American Count"]
	return p2, p22