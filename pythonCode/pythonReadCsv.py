import pandas as pd

data = pd.read_csv("DataScienceDay3/data.csv")
data = data.head(10)

print(data.to_string())