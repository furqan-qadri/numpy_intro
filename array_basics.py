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

for x in np.nditer(array1, flags=['buffered'], op_dtypes=['S']):
    print(type(x))