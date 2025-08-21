###               Goal: Why libraries matters and how logic translates
# # Pure Python 
import csv
with open ("C:\\Users\\91905\\Downloads\\iris.csv") as f:
    reader = csv.reader(f)
    data = list(reader)

header = data[0]
rows = data[1:]
print(f"Columns:{header}")
print(f"Number of columns: {len(header)}")
print(f"Number of rows: {len(rows)}")
print([i for i in data if data is None])

col_index = 0
values = [float(row[col_index]) for row in rows if row[col_index] != "" ]
print("Minimum:",min(values))
print("Maximum: ",max(values))
print("Mean:",sum(values)/len(values))
print([i for i in values if i is None])


# # Python Pandas
import pandas as pd
data = pd.read_csv("C:\\Users\\91905\\Downloads\\iris.csv")
print(data.head())
print(data.columns)
print(len(data.columns))
print(len(data.loc[:]))
print(len(pd.isnull(data)))

print(data.iloc[:,1:5].min())
print(data.iloc[:,1:5].max())
print(data.iloc[:,1:5].mean())