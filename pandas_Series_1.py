import numpy as np
import pandas as pd
# data = np.array([1, 2, 3])
data = {'A1': 1, 'A2': 2, 'A3': 3}

#index = ['A1', 'A2', 'A3']
ser = pd.Series(data)
#print(data)
print(ser)