import matplotlib.pyplot as plt



grade=["one","two","three","four","five"]
students =[10,25,37,48,69]

plt.subplot(131)
plt.bar(grade,students)
plt.subplot(132)
plt.scatter(grade,students)
plt.subplot(133)
plt.plot(grade,students)

plt.suptitle("working with different ploting")
plt.show()