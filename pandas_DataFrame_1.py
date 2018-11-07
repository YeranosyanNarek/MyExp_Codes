import numpy as np
import pandas as pd

#data = [['Alex1', 1], ['Alex2', 2], ['Alex3', 3], ['Alex4', 4], ['Alex5', 5]]
data = {'Name': ['Alex1', 'Alex2', 'Alex3', 'Alex4', 'Alex5'],
        'Age': [1, 2, 3, 4, 5]}
#data = {'A1':1, 'A2':2, 'A3':3}
"""
data = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
"""
index = ['Ps1', 'Ps_2', 'Ps_3', 'Ps_4', 'Ps_5']
#data_frame = pd.DataFrame(data, index=index, columns=['Name', 'Age'], dtype=float)
data_frame = pd.DataFrame(data, index=index)
#print(data)
print(data_frame)






