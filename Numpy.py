# what is numpy?
# Numpy is a library in python which is used for numerical computations. It is used for working with arrays.
# It also has functions for working in domain of linear algebra, fourier transform, and matrices.


# Why use Numpy?
# Numpy is faster than the traditional python lists.
# It uses less memory as compared to python lists.
# It is convenient to use.



# import numpy as np

# a = np.array([1, 2, 3])
# b = np.array([[1, 2], [3, 4]])

# print(a)
# print(b)

# import numpy as np

# c = np.zeros((4,5,6))
# print(c.ndim)


#Initializing Arrays in Numpy with Ones np.ones()
# import numpy as np
# a = np.ones((5,6))  # 5 is row and 6 is column
# print(a)



#It gives diagnonal array
# import numpy as np
# a=np.eye(3)
# print(a)


# Creating sequence with np.arange()
#Arange function create an array in range(start,end,step) -->Exclusive

# import numpy as np
# a=np.arange(1,13).reshape(3,4)              # Reshape function is used to change the shape of array
# print(a)                     # from 1d to 2d array using reshape.


# import numpy as np
# a=np.arange(1,13).reshape(2,6)
# print(a)

#12 --> 2,6,4,3
# reshape --> factor --> m*n --> total number of elements.

# Creating Evenly space
# import numpy as np
# a=np.linspace(10,20,5)   # start , end , number of elements
# print(a)
# np.linspace() is incredily useful for creating arrays with a specified number of evenly spaced values over a given interval.The stop svalue is inclusive, meaning it is included in the generated array.



# Specifying data types(dtype) during array creation
# import numpy as np
# a=np.ones((3,4), dtype=str)
# print(a)



# Basic array operation
# import numpy as np
# a = np.linspace(10,20,12).reshape(3,4)
# b = np.linspace(30,40,12).reshape(3,4)
# print(a,b)

# a + 1
# print(a)


