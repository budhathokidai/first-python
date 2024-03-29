import matplotlib.pyplot as plt
import numpy as np

y=np.array([90,70,80,92])
mylabels=["c++","javascript","html","python"]
plt.pie(y,labels=mylabels,startangle=90)
plt.show()
