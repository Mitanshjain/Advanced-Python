# pandas => pandas is a library which is used to manipulate the data, and analyze the data.
# PAndas is build on the top of numpy library.


# To install pandas we use the pip command. => python -m pip install pandas

# import pandas as pd


# # to read the csv files we use the read_csv method
# pd.read_csv('')

# import pandas as pd
# print(pd.__version__) To check the version of pandas.



# import pandas as pd
# df = pd.read_csv(r"C:\Users\MY PC\Downloads\mnist_test.csv")
# print(df.head())
# This is for only five rows in which we use word head.


# This is for max rows print in excel.
# pd.set_option('display.max_rows', None)
# print(df)


# A pandas Series is a one-dimensional, labled array that offers additional features like explicit indexing and integrated missing data handling, making it ideal for data analysis.

# Creating a series with the help of dictonary
# import pandas as pd
# d = {
#     'a':10,
#     'b':20,
#     'c':30,
#     'd':40
# }

# print(pd.Series(d))
# when we create any Series with the help of dictonary 
# Key -> index,, value -> value

# import pandas as pd
# d = {
#     'a':10,
#     'b':20,
#     'c':30,
#     'd':40
# }
# s1 = pd.Series(d)
# print(s1.values)   # It gives array or list.
# .values is used to retrive the value of the series 
# It returns the value into the form of numpy array


# .index is used to retrive the index of the series
# import pandas as pd
# d = {
#     'a':10,
#     'b':20,
#     'c':30,
#     'd':40
# }
# s1 = pd.Series(d)
# print(s1.index)   # It gives index of the series.





# Creating a series with the help of list
# import pandas as pd
# list = [10,20,30,40]
# print(pd.Series(list))

# Creating a series with the help of numpy array
# import pandas as pd
# import numpy as np
# arr = np.array([10,20,30,40])
# print(pd.Series(arr))



# Vectorized operations in pandas Series
# import pandas as pd
# s1 = pd.Series([10,20,30,40])
# s2 = pd.Series([1,2,3,4])
# print(s1 + s2) we can do all the arithmetic operations like +,-,*,/ etc..


# Accessing elements in pandas Series
# import pandas as pd
# import numpy as np
# s1 = pd.Series(np.arange(1,13))
# print(Series)

# print(series[series > 5])


# A pandas Dataframe is a primary two dimensional, table like data structure used for data manipulation and analysisi in python.
# Key components:- 
# Data => The actual value contained within the table.
# Rows => Labeled observation (also called index).
# Columns => Labeled attributes (also called features).(Like number ,text etc).


# Creating a Dataframe with the help of dictonary
# import pandas as pd
# details = {
#     'Name':['Aman','Rohan','Sohan','Mohan'],
#     'Subject':['Maths','Science','English','Hindi'],
#     'Marks':[90,85,88,92],
#     'Address':['Delhi','Mumbai','Kolkata','Chennai']
# }
# df = pd.DataFrame(details,index = ['a','b','c','d']) # By default index is 0 to 3 when we give indexes then it will replace the default index.
# print(df)


# Creating a Dataframe with the help of list
# import pandas as pd
# details = [
#     ['Aman','Maths',90,'Delhi'],
#     ['Rohan','Science',85,'Mumbai'],
#     ['Sohan','English',88,'Kolkata'],
#     ['Mohan','Hindi',92,'Chennai']
# ]
# df = pd.DataFrame(details,columns=['Name','Subject','Marks','Address'],index=['a','b','c','d'])
# print(df)


# Creating a series with the help of numpy array
# Importing pandas and numpy
# Indices are from 0 to n-1
# import pandas as pd 
# import numpy as np
# Series = pd.Series(np.arange(1,13))
# print(Series)



# Coverting a dataFrame to csv file/format
# import pandas as pd
# details = {
#     'Name':['Aman','Rohan','Sohan','Mohan'],
#     'Subject':['Maths','Science','English','Hindi'],
#     'Marks':[90,85,88,92],
#     'Address':['Delhi','Mumbai','Kolkata','Chennai']
# }
# df = pd.DataFrame(details,index = ['a','b','c','d'])
# df.to_csv('student_details.csv')  # It will convert the dataframe into csv file.

# Pandas => Read, csv, read_csv('path')
# Write => to_csv -> apply on the data frame



# We can also convert a dataframe to excel as well.
# import pandas as pd
# details = {
#     'Name':['Aman','Rohan','Sohan','Mohan'],
#     'Subject':['Maths','Science','English','Hindi'],
#     'Marks':[90,85,88,92],
#     'Address':['Delhi','Mumbai','Kolkata','Chennai']
# }
# df = pd.DataFrame(details,index = ['a','b','c','d'])
# df.to_excel('student_details.xlsx')  # It will convert the dataframe into excel file.



# import pandas as pd
# df = pd.read_csv(r"C:\Users\MY PC\Downloads\california_housing_test.csv")
# print(df.columns)                   # df.columns is used to retrive the columns of the dataframe.

# # We can also select multiple columns as well.

# # print(df[['longitude','latitude','housing_median_age']])

# # print(df[['longitude']])
# # It will give the output for single column in the form of dataframe.


# # print(df.loc[0])                    # By using loc we can access the rows by index labels.
#                                       # It will give the output for single row in the form of series.
# # print(df.loc[0:6])                  # It will give the output for multiple rows in the form of dataframe.

# print(df.loc[0:6, ['longitude','latitude','housing_median_age']])  # It will give the output for multiple rows and multiple columns in the form of dataframe.


# import pandas as pd
# details = {
#     'Name':['Aman','Rohan','Sohan','Mohan'],
#     'Subject':['Maths','Science','English','Hindi'],
#     'Marks':[90,85,88,92],
#     'Address':['Delhi','Mumbai','Kolkata','Chennai']
# }
# df = pd.DataFrame(details,index = ['a','b','c','d']) # By default index is 0 to 3 when we give indexes then it will replace the default index.
# print(df.loc[['a','b','c'],['Subject','Marks']])

# By using loc we can access the rows by index labels.




# Select all rows of the dataframe and also select three any colums.
# import pandas as pd
# details = {
#     'Name':['Aman','Rohan','Sohan','Mohan'],
#     'Subject':['Maths','Science','English','Hindi'],
#     'Marks':[90,85,88,92],
#     'Address':['Delhi','Mumbai','Kolkata','Chennai']
# }
# df = pd.DataFrame(details,index=['a','b','c','d']) # By default index is 0 to 3 when we give indexes then it will replace the default index.
# print(df.loc[['a','b','c','d'],['Name','Subject','Marks']]) # selecting tree colums and all rows.



# .loc[] is used to access the rows by index labels.
# .iloc[] is used to access the rows by index position.

# Key feature of .loc[]
# Label-Based:- It uses the actual row and column labels, not therir integer positions(which is what .iloc[] is for).

# Inclusive Slicing :- Unlike standard python slicing, when using a slice with .loc[](eg., 'start_label' : 'end_label'), both the start and the stop label are included in the selection.



# .iloc[] => Integer based indexing
# import pandas as pd
# details = {
#     'Name':['Aman','Rohan','Sohan','Mohan'],
#     'Subject':['Maths','Science','English','Hindi'],
#     'Marks':[90,85,88,92],
#     'Address':['Delhi','Mumbai','Kolkata','Chennai']
# }
# df = pd.DataFrame(details,index=['a','b','c','d']) # By default index is 0 to 3 when we give indexes then it will replace the default index.
# print(df.iloc[['a','b','c','d'],['Name','Subject','Marks']])



# import pandas as pd 
# df = pd.read_csv(r"C:\Users\MY PC\Downloads\california_housing_test.csv")
# print(df)

# import pandas as pd 
# df = pd.read_csv(r"C:\Users\MY PC\Downloads\california_housing_test.csv")
# print(df.head)
# head() method is used to print the first five rows of the dataframe.


# import pandas as pd 
# df = pd.read_csv(r"C:\Users\MY PC\Downloads\california_housing_test.csv")
# print(df.sample(10))
# sample() method is used to print the random rows of the dataframe.
# Here 10 random rows will be printed.
# but if we have n rows from the dataframe we use df.sample(n).


# import numpy as np
# import pandas as pd
# df = pd.read_csv(r"C:\Users\MY PC\Downloads\california_housing_test.csv")
# np.random.seed(43)
# # print(df.sample(10))
# print(df.tail())

# df.tail() method is used to print the last five rows of the dataframe.



# import pandas as pd
# df = pd.read_csv(r"C:\Users\MY PC\Downloads\california_housing_test.csv")
# print(df.info())
# df.info() method is used to print the summary of the dataframe.


# import pandas as pd
# df = pd.read_csv(r"C:\Users\MY PC\Downloads\california_housing_test.csv")
# print(df.describe())

# df.describe() method is used to print the statistical summary of the dataframe.
# It includes measures like count, mean, std deviation, min, max, and quartiles for numerical columns.
# df.describe is used to show five point summary of the data or it show the statistical property of the data on the numerical columns.
# five point summary:-
# 1. minimum => min => 0th percentile
# 2. first quartile => 25th percentile
# 3. median => second quartile => 50th percentile
# 4. third quartile => 75th percentile
# 5. maximum => 100th percentile

# count => shows the total number of entries
# it shows the mean and standard deviation of the numerical column.


# import pandas as pd
# df = pd.read_csv(r"C:\Users\MY PC\Downloads\california_housing_test.csv")
# print(df.isna().sum())

# df.isna() => return true or false by checking wheather the row entry is null or not => if the row entry is null then it return true
# if row entry is not null then it return false

# df.isna().sum() => it return the total number of null values from the data frame along with their column names.

# import pandas as pd
# df = pd.read_csv(r"C:\Users\MY PC\Downloads\california_housing_test.csv")
# print(df.fillna(df['median_house_value']))

# import pandas as pd
# df = pd.read_csv(r"C:\Users\MY PC\Downloads\california_housing_test.csv")
# print(df['median_house_value'].unique())
# df['median_house_value'].unique() => to find the all categories of the dataframe we use .unique() method it return an array of category.



