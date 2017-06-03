line_str = '/Users/Jayalakshmi/Desktop/geo.txt'

import json
import pandas as pd

array=[]

with open(line_str) as f:
    for line in f:
    	array.append(line)

#extracting city and state name from location
data=[]

x=len(array)
for i in range (0,x):
	data = json.loads(array[i])
	
	str1=data[17:]
	pos= str1.find("\'")
	data.append(str1[:pos])
	

print data
df = pd.DataFrame(data)
print df
df.to_csv("city_state.csv",encoding='utf8', index=False)