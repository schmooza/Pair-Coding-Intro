import pandas as pd
import pygal
import cairosvg

from person01 import *
from person02 import *


print("\n This program loads two sets of data and combines them into one file, check the outputData folder to see the result. \n")


print("Below is the data selected.\nTry selecting different data.\n")
outputp1 = loadDataPerson01()
# print (outputp1,"data selected by person 1")

outputp2 = loadDataPerson02()
# print (outputp2, "data selected by person 2")


#joins the data together
finalOutput = pd.concat([outputp1, outputp2], axis=1)

print(finalOutput)

print ("\n Now lets sort the data.")
f2 = finalOutput.sort_values(by=['Multi-race Count', 'Female Count'])



print(f2)


#stuff all the data into a file.

# index=False removes the index numbers as they are mixed up.

f2.to_csv('outputData/outputfile_2sets.csv',index=False)



#converts data into lists, pygal likes lists.

outputp1 = outputp1.values.tolist()
outputp2 = outputp2.values.tolist()
f2 = f2.values.tolist()


print("\nNext it takes the selected data and makes a graph. Check the image file for results.")
treemap = pygal.Treemap()
treemap.title = '2 things compared for some reason'
treemap.add('Female Count', outputp1)
treemap.add('Multi-race Count', outputp2)

treemap.render_to_png('images/myGraph.png')


scatter = pygal.XY(stroke=False)
scatter.title = 'Correlation'
scatter.add('Female Count', f2)
scatter.add('Multi-race Count', f2)

scatter.render_to_png('images/myGraph2.png')