import matplotlib.pyplot as plt

y=["R","A","B","I"]
X=[10,24,35,89]
plt.pie(X,labels=y,autopct="%1.1f%%",startangle=45)

plt.title("pie Chart")
plt.show()