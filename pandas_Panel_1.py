import numpy as np
import pandas as pd
data = {'item1': pd.DataFrame(np.random.randn(4, 3)),
        'item2': pd.DataFrame(np.random.randn(4, 2))
        }

panel = pd.Panel(data)

print(panel)
print(panel.major_xs(1))






