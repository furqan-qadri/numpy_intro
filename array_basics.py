import numpy as np

array1=np.array([[1,2,3],[2,3,4]])
# print(array1.size)


# array1=np.array([1,2,3,4,5])

array2=np.array([6,7,8,9,10])

# sum_array=array1+array2
# difference_array=array1-array2
# product_array=array1*array2
# ratio_array=array1/array2
# print(sum_array,difference_array,product_array,ratio_array)

# iterate through each and change the data type of each value

# for x in np.nditer(array1, flags=['buffered'], op_dtypes=['S']):
    # print((x))
    
array3=np.array_split(array1,3)
array4 = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])

# print(array3)
# array4=np.vsplit(array4,2)
# print(array4)


x=np.where(array2==7)
# print(x)

array7=np.arange(100,200,10)
array7=array7.reshape(2,5)
# print(array7)


# Exercise 4: Return array of odd rows and even columns from below numpy array
sampleArray = np.array([[3 ,6, 9, 12], [15 ,18, 21, 24], 
[27 ,30, 33, 36], [39 ,42, 45, 48], [51 ,54, 57, 60]])

# print(sampleArray)

# Exercise 5: Create a result array by adding the following two NumPy arrays. Next, modify the result array by calculating the square of each element

arrayOne = np.array([[5, 6, 9], [21 ,18, 27]])
arrayTwo = np.array([[15 ,33, 24], [4 ,7, 1]])


arrayThree=arrayOne+(arrayTwo)
arrayThree=arrayThree**2
arrayFlat=arrayThree.ravel()
print(arrayOne.ravel())
