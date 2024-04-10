import numpy as np
#1d
a= np.arange(5)
print(a)

#2d

b=np.arange(5).reshape(1,5)
print(b)


#3d

c=np.arange(20).reshape(2,2,5)
print(c)

# Sort array
array = np.array([1, 32, 2, 6, 11, 5])
sort_array = np.sort(array)
print("The sort array  is \n ", sort_array)

# slicing
slice_array = np.arange(10) ** 2
print("The array is\n", slice_array)
print(" every second element from the beginning of the list\n", slice_array[::2], "\n")  # get every second element from the beginning of the list
print("Sliceing array is\n", slice_array[2:7])

for i in slice_array:
    print(i, "\t", i * 2)
