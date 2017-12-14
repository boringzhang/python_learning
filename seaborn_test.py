import numpy as np
import matplotlib.pyplot as plt  
np.random.seed(0)
import seaborn as sns;sns.set()

uniform_data = np.random.rand(100, 200)
print(uniform_data)
ax = sns.heatmap(uniform_data)

plt.show()