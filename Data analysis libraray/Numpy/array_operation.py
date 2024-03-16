import  numpy  as np

array1 =[4,5,6]
array2 =[7,8,9]

#Adding arrays using + operator
result =array1 + array2
print(f"Result of adding two arrays: \n{result}")

#multiplication
mul =np.dot(array1,array2)
print(f"multiplication of two ARRAY: \n{mul}")


#indexing of array

firstindex = array1[0]
print(f"\n indexed value :\n {firstindex} ")

secondindex =array2[2]
print(f"\n value indexed : \n {secondindex}")


#slicing of an array
slicedarray=np.array(["hello","my","name","is","Rabi","Budhathoki"])
print("\n slicing")
print("full array : \n",slicedarray)
print("from start to fourth index :\n",slicedarray[0:4])


first_element = slicedarray[:1]  # Get elements from beginning to the first occurrence of non-True element in
print(first_element)


array = [1, 2, 3, 23, 5]
sum = np.sum(array)
print(f"The sum of the array \n {sum}")
