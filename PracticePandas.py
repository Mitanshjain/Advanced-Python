# Part 1: Basic Pandas Operations
# 1. Load the dataset using Pandas.
# import pandas as pd
# df = pd.read_csv("StudentsPerformance.csv")
# print(df)



# 2. Display the first 5 rows of the dataset.
# import pandas as pd
# df = pd.read_csv("StudentsPerformance.csv")
# print(df.head())



# 3. Display the last 5 rows of the dataset.
# import pandas as pd
# df = pd.read_csv("StudentsPerformance.csv")
# print(df.tail())



# 4. Check the shape, size, and ndim attributes of the DataFrame.
# import pandas as pd
# df = pd.read_csv("StudentsPerformance.csv")
# print("shape is :",df.shape)
# print("Size is :",df.size)
# print("ndim is:",df.ndim)



# 5. Display the column names.
# import pandas as pd
# df = pd.read_csv("StudentsPerformance.csv")
# print("column is:",df.columns)



# 6. Check the data types of all columns.
# import pandas as pd
# df = pd.read_csv("StudentsPerformance.csv")
# print(df.dtypes)



# 7. Check for any missing values in the dataset.
# import pandas as pd
# df = pd.read_csv("StudentsPerformance.csv")
# print(df.isna().sum())



# 8. Select and display only the math score and reading score columns.
# import pandas as pd
# df = pd.read_csv("StudentsPerformance.csv")
# print(df['math score'],['reading score'])



# 9. Find the number of male and female students (count of each gender).
# import pandas as pd
# df = pd.read_csv("StudentsPerformance.csv")
# print(df['gender'].value_counts())



# 10. Find the unique values present in the lunch column.
# import pandas as pd
# df = pd.read_csv("StudentsPerformance.csv")
# print(df['lunch'].unique())


# Part 2: Filtering Questions

# 1. Find and display the records of students who scored more than 80 in math score.
# import pandas as pd
# df = pd.read_csv("StudentsPerformance.csv")
# print(df[(df['math score']>80)])



# 2. Find and display the records of students who scored less than 50 in writing score.
# import pandas as pd
# df = pd.read_csv("StudentsPerformance.csv")
# print(df[(df['writing score']<50)])



# 3. Filter and display the students who completed the test preparation course.
# import pandas as pd
# df = pd.read_csv("StudentsPerformance.csv")
# print(df[df['test preparation course']=='completed'])



# 4. Find and display the records of female students with a reading score greater than 70.
# import pandas as pd
# df = pd.read_csv("StudentsPerformance.csv")
# result = df[(df['gender'] == 'female') & (df['reading score'] > 70)]
# print(result)



# 5 Find and display the records of students who got free/reduced lunch.
# import pandas as pd
# df = pd.read_csv("StudentsPerformance.csv")
# result = df[df['lunch'] == 'free/reduced']
# print(result)



# Part 3: Basic Aggregation
# 1. Find the average of the math score.
# import pandas as pd
# df = pd.read_csv("StudentsPerformance.csv")
# average_math_score = df['math score'].mean()
# print("Average Math Score:", average_math_score)


# 2. Find the maximum and minimum values in the reading score column.
# import pandas as pd

# df = pd.read_csv("StudentsPerformance.csv")

# max_reading = df['reading score'].max()
# min_reading = df['reading score'].min()

# print("Maximum Reading Score:", max_reading)
# print("Minimum Reading Score:", min_reading)



# 3 Count the number of students grouped by race/ethnicity.
# import pandas as pd

# df = pd.read_csv("StudentsPerformance.csv")

# race_counts = df.groupby('race/ethnicity').size()
# print(race_counts)



# 4. Find the average writing score grouped by gender.
# import pandas as pd

# df = pd.read_csv("StudentsPerformance.csv")

# avg_writing_by_gender = df.groupby('gender')['writing score'].mean()
# print(avg_writing_by_gender)



# 5 Sort the students by math score in descending order and display the top 10.
# import pandas as pd

# df = pd.read_csv("StudentsPerformance.csv")

# top_10_math = df.sort_values(by='math score', ascending=False).head(10)
# print(top_10_math)



# Part 4: Beginner Friendly Tasks

# 1. Create a new column named total_score, which is the sum of math score, reading score, and writing score.
# import pandas as pd

# df = pd.read_csv("StudentsPerformance.csv")

# df['total_score'] = (
#     df['math score'] +
#     df['reading score'] +
#     df['writing score']
# )

# print(df.head())



# 2.Create a new column named average_score (total score divided by 3).
# import pandas as pd

# df = pd.read_csv("StudentsPerformance.csv")
# df['total_score'] = (
#     df['math score'] +
#     df['reading score'] +
#     df['writing score']
# )

# df['average_score'] = df['total_score'] / 3

# print(df)



# 3. Add a column named result. A student passes if their average_score is 60 or above; otherwise, they fail. (Hint: Use a conditional function or lambda expression).
# import pandas as pd

# df = pd.read_csv("StudentsPerformance.csv")
# df['total_score'] = (
#     df['math score'] +
#     df['reading score'] +
#     df['writing score']
# )
# df['average_score'] = df['total_score'] / 3
# df['result'] = df['average_score'].apply(lambda x: 'Pass' if x >= 60 else 'Fail')

# print(df[['average_score', 'result']].head())



# 4. Find the top 5 students based on their total_score.
# import pandas as pd

# df = pd.read_csv("StudentsPerformance.csv")
# df['total_score'] = (
#     df['math score'] +
#     df['reading score'] +
#     df['writing score']
# )

# df['total_score'] = df['math score'] + df['reading score'] + df['writing score']

# top_5_students = df.sort_values(by='total_score', ascending=False).head(5)
# print(top_5_students)



# 5. Find the bottom 5 students based on their math score.
# import pandas as pd

# df = pd.read_csv("StudentsPerformance.csv")

# bottom_5_math = df.nsmallest(5, 'math score')
# print(bottom_5_math)
