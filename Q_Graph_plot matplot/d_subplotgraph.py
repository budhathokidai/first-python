import matplotlib.pyplot as plt
import numpy as np

# its first plot
x=np.array([1,2,3,4])
y=np.array([5,6,7,8])

plt.subplot(1,2,1)
plt.plot(x,y)



#its second plot

x=np.array([0,1,2,3,4,5,6])
y=x+3

plt.subplot(1,2,2)
plt.plot(x,y,marker="o")
#adding title and labels to the plots
plt.title("My First Plot")
plt.xlabel("x_axis")
plt.ylabel("y_axis")
print("done")
#showing all the plots at once
plt.show()