# PANDAS

# What is series ?
# Series => 1D array with labels
# DataFrame => 2D array with labels

# import pandas as pd
# import numpy as np


# df=pd.Series(np.array([1,2,3,4,5,6,7,8,9,10]))
# print(df[df%2 == 0])


# import pandas as pd
# import numpy as np
# data = [x for x in range(10,101)]
# my_data = pd.Series(data)
# odd_series = my_data[my_data%2 !=0]
# scaler_data = odd_series+5
# print(scaler_data)




# import pandas as pd
# data = {
#     'Name':['Alice','Bob','charlie','david'],
#     'Age':[24,27,22,32],
#     'city': ['New York','Los','Alwar','Houston'],
#     'gender':['Male','Female','Male','Male']
# }

# df = pd.DataFrame(data, index=['a','b','c','d'])
# print(df.loc[['a','b','c','d']]) # To access the rows by using .loc.
# print(df.iloc[0:4,0:2]) # to access rows and columns by using iloc with slicing[row_slicing,column_slicing]

# print(df.iloc[2:4,2:4]) # to getting last two rows and last two columns



# Add new colums inside the dataframe
# df['occupation'] = pd.Series(['Students', 'Working Professional', 'Teachers','Engineers'])
# print(df)




# print("Dataframe from dictonary of list:",df['Age'].mean())
# print("Dataframe from dictonary of list:",df['Age'].median())
# print("Dataframe from dictonary of list:",df['gender'].mode())



#.loc is primarily label-based indexing
#.iloc is primarily integer based indexing


# .loc[0] for one column
# .loc[[0,1]] for multiple column
# .loc[['a','b'],['Name','city']]








# df.reset_index()
#identify the categorical columns and numerical columns 
# Show the highest marks of math,science, social science


import pandas as pd
import numpy as np
data = {
    'Name':['Alice','Bob','charlie','david','Eve','Frank'],
    'Age':[24,27,22,32,39,46],
    'city': ['New York','Los','Alwar','Houston','Bharatpur','Dausa'],
    'gender':['Male','Female','Male','Male','Female','Male'],
    'math':[78,87,98,88,79,90],
    'Science':[78,90,80,85,np.nan,87],
    'Social Science':[78,89,90,87,98,95]

}
df = pd.DataFrame(data, index=['a','b','c','d','e','f'])

# print(df)
# print(df.dropna()) to drop nan value with row
