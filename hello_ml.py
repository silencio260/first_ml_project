import numpy as np
##import matplotlib.pylot as mpt
import pandas as pd

data_set = pd.read_csv('Data.csv')

print(data_set)

x = data_set.iloc[:, :-1].values

print(x)

y = data_set.iloc[:,3].values

print(y)