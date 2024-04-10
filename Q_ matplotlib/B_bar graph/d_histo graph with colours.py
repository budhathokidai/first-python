import matplotlib.pyplot as plt
import numpy as np

#data

np.random.seed(0)
data=np.random.randn(1000)

#plot the histogram
plt.hist(data,bins=30,color="black")
