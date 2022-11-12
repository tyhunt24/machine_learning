import pandas as pd

data = pd.read_csv("syndata.csv", header = None)

print(data.sum(axis=1))