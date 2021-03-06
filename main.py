import pandas as pd
import pygal
import cairosvg

from person01 import *
from person02 import *


print("\n This program loads two sets of data and combines them into one file, check the outputData folder to see the result. \n")


print("Below is the data selected.\nTry selecting different data.\n")
outputp1, outputp11 = loadDataPerson01()
# print (outputp1,"data selected by person 1")

outputp2, outputp22 = loadDataPerson02()
# print (outputp2, "data selected by person 2")


#joins the data together
finalOutput = pd.concat([outputp1,outputp11, outputp2,outputp22], axis=1)



totalFems = outputp1.sum()
print(totalFems,"total femals in NY")


print(finalOutput)

print ("\n Now lets sort the data.")
f2 = finalOutput.sort_values(by=['Asian Count', 'Black or African American Count'])



print(f2)


#stuff all the data into a file.

# index=False removes the index numbers as they are mixed up.

f2.to_csv('outputData/outputfile_2sets.csv',index=False)



#converts data into lists, pygal likes lists.

outputp1 = outputp1.values.tolist()
outputp11 = outputp11.values.tolist()

outputp2 = outputp2.values.tolist()
outputp22 = outputp22.values.tolist()

pairsGroup1= list(zip(outputp1,outputp11))
# print(pairsGroup1,"debug ")
pairsGroup2= list(zip(outputp2,outputp22))

print("\nNext it takes the selected data and makes a graph. Check the image file for results.")

treemap = pygal.Treemap()
treemap.title = '2 things compared for some reason'
treemap.add('Female Count', outputp1)
treemap.add('Female Asains', outputp11)
treemap.add('Male Count', outputp2)
treemap.add('Black Females', outputp22)

treemap.render_to_png('images/myGraph.png')


scatter = pygal.XY(stroke=False)
scatter.title = 'Correlation of Gender to Race'
scatter.x_title='Gender Amount Per Area of NY'
scatter.y_title='Race Amount Per Area of NY'

scatter.add('Asain Females', pairsGroup1)
scatter.add('Black Females', pairsGroup2)

scatter.render_to_png('images/myGraph2.png')