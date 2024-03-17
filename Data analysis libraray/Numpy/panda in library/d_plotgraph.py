import pandas as pd
import matplotlib.pyplot as plt

data= pd.read_csv(
    "C:/Users/brobu/OneDrive/Documents/Python/sample_datasets.csv"
)

#print(data)

data.plot()
plt.show()