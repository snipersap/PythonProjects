#Arrays in Python with numpy
import numpy as np
print(np.__version__)

#sample array definitions
sample_array = np.array([1,2,3,4,5])
print(sample_array,"of type:",type(sample_array))

tuple_array = np.array((1,2,3,4,5))
print(tuple_array,"of type:",type(tuple_array),"with dimension:",tuple_array.ndim)

dict_array_0d = np.array({1,2,3,5,6,"hello"})
print(dict_array_0d,"of type:",type(dict_array_0d),"with dimension:",dict_array_0d.ndim)

dict_array_2d = np.array([[{1,2,3,5,6}],[{7,8,9,0,5,"hello"}]])
print(dict_array_2d,"of type:",type(dict_array_2d),"with dimension:",dict_array_2d.ndim)

array_2d = np.array([[1,2,3],[4,5,6]])
array_3d = np.array([[[1,2,4],[5,6,7]],[[10,20,30],[33,44,55]]])
print(array_2d,"of type:",type(array_2d),"with dimension:",array_2d.ndim)
print(array_3d,"of type:",type(array_3d),"with dimension:",array_3d.ndim)

#Extracting array elements
print("dict_array_0d:",dict_array_0d)
print("Showing tuple_array elements one by one:",tuple_array[0], tuple_array[1], tuple_array[2],tuple_array[3:5])
print("array_2d[0,2] should be 3:",array_2d[0,2])
print("array_3d[1,1,1] should be 44:",array_3d[1,1,1])

#Array slice
print("array_3d[1,0,0:]:",array_3d[1,0,0:])     #From:till end of array
print("array_3d[1,0,:2]:",array_3d[1,0,:2])     #Upto :end (end index not included)
print("array_3d[1,0,:-1]:",array_3d[1,0,:-1])     #Upto :end-1 index (end-1 index not included)

#Further functions with array
#Create array with linespace
linspace_array = np.linspace(0,15,16)
print(linspace_array)

#TODO>>


