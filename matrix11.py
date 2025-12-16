# Slicing in matrix

# import numpy as np
# matrix = np.arange(1,13).reshape(3,4)
# print(matrix)

# [[ 1  2  3  4]  This is the matrix output
#  [ 5  6  7  8]
#  [ 9 10 11 12]]


# print("array =>",matrix[0])
# print("array =>",matrix[1])
# print("array =>",matrix[2])


# print("new matrix =>",matrix[0][0:3])  # This is for row

# print("For row elements",matrix[0,:]) # This is for row elements

# print("For column",matrix[:,1]) # this is for column

# print("For specific element in matrix",matrix[1,1])

# print("For two column",matrix[:,0:2])


# matrix[:] => it will access whole rows
# matrix[:,0:2] => This will give the first two columns
# matrix[0,:] => This will give the first row


# print(matrix[1:3,2:])

# Random in numpy module is used to generate the random number.
# Randint => It is used to generate the random integer number in the given range.

# import numpy as np
# np.random.seed(23) seed => It is used to initialize the random number generator but its fixed.
# print(np.random.randint(1,10,3))

# Into this the start is inclusive
# End is exclusive


# import numpy as np
# print(np.random.rand(40))

# np.randdom.rand is used to genrate the value between 0 to 1
# Into this function or method we pass the number or element which we want to generate.

# import numpy as np
# s = np.array([1,2,3,4])
# np.float64(2.5)

# import numpy as np
# n = np.random.randint(1,10,50)
# np.median(n)
# print(n)

# import numpy as np
# n = np.random.randint(1,10,50)
# np.mean(n)
# print(n)

# import numpy as np
# n = np.array([1,2,3,4,5,6])
# print(np.median(n))

# import numpy as np
# m = np.random.randint(1,10,12).reshape(3,4)
# print(m)
# flatten_matrix = m.flatten()
# print(flatten_matrix)
# Flatten is used to convert 2d array into 1d array.

# Generate a matrix using the random module randint, last column.
# 2d elements => mean => flatten => mean.

# import numpy as np
# m = np.random.randint(1,10,12).reshape(3,4)
# print(m)
# print("matrix =>",m[:,2:4])  # It extract last two column.


# Diffrence between flatten and ravel
# Flatten => It returns a copy of the original array and any modifications made to the flattened array do not affect the original array.
# Ravel => It returns a flattened array as a view of the original array whenever possible. Modifications made to the raveled array may affect the original array.

