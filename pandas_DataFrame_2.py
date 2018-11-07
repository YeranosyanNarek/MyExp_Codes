import numpy as np
import pandas as pd

data = {'one': pd.Series([1, 2, 3], index=['a', 'b', 'c']),
        'two': pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
        }
data_frame = pd.DataFrame(data)

# Adding a new column to an existing DataFrame object with column label by passing new series
data_frame['there'] = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
print('Adding a new column by passing as Series')
print(data_frame)

print('Adding a new column using the existing columns in DataFrame')

data_frame['four'] = data_frame['one'] + data_frame['there']
print(data_frame)