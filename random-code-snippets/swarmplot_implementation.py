import seaborn
import pandas
import matplotlib.pyplot as plt


csv = seaborn.load_dataset("tips")
res = seaborn.swarmplot(x="tip", y="sex", data=csv)

plt.show()