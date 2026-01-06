#mini project - user loads a CSV and script 
#auto plots histogram bar chart + summary 


#imports libraries

import pandas as pd
import json 
import matplotlib.pyplot as plt


#takes user input and validates input

file = input("enter a file with .csv or .json")

if file.endswith(".csv"):
    df = pd.read_csv(file)

elif file.endswith(".json"):
    df = pd.read_json(file)

else:
    print("file type is unsupported")    
    exit()

#print 5 lines
print("\n---5 rows--")
print(df.head())

#prints summary 
print("\n--- summary statistics---")
print(df.describe())

#prints bar chart
df.plot(kind="bar")
plt.title("bar chart of numeric columns")
plt.tight_layout()
plt.show()

#histogram
df.hist()
plt.suptitle("histograms of numeric columns")
plt.tight_layout()
plt.show()


