# 1. Load the Titanic dataset into a pandas DataFrame.
# import pandas as pd
# df = pd.read_csv('archive (1)\Titanic-Dataset.csv')
# print(df)


# 2. Display the first 5 rows of the DataFrame.
# import pandas as pd
# df = pd.read_csv('archive (1)\Titanic-Dataset.csv')
# print(df.head())

# 3. Display the last 5 rows of the DataFrame.
# import pandas as pd
# df = pd.read_csv('archive (1)\Titanic-Dataset.csv')
# print(df.tail())


# 4. Print the number of rows and columns in the dataset.
# import pandas as pd
# df = pd.read_csv('archive (1)\Titanic-Dataset.csv')
# print(df.shape)


# 5. Display all column names and their data types.
# import pandas as pd
# df = pd.read_csv('archive (1)\Titanic-Dataset.csv')
# print(df.columns)

# Dtype
# import pandas as pd
# df = pd.read_csv('archive (1)\Titanic-Dataset.csv')
# print(df.dtypes)

# 6. Show a statistical summary of all numerical columns
# import pandas as pd
# df = pd.read_csv('archive (1)\Titanic-Dataset.csv')
# print(df.describe)


# 7. Show the count of non-null values per column.
# import pandas as pd
# df = pd.read_csv('archive (1)\Titanic-Dataset.csv')
# print(df.count)


# SECTION B — MISSING VALUES & CLEANING:-

# 1. Identify which columns contain missing values.
# import pandas as pd
# df = pd.read_csv('archive (1)\Titanic-Dataset.csv')
# print(df.isna().any())


# 2. Count missing values in each column
# import pandas as pd
# df = pd.read_csv('archive (1)\Titanic-Dataset.csv')
# print(df.isna().sum())


# 3. Drop the Cabin column from the DataFrame
# import pandas as pd
# df = pd.read_csv(r'archive (1)\Titanic-Dataset.csv')
# df1 = df.drop(columns=['Cabin'])
# print(df1)


# 4. Fill missing values in Age with the mean age
# import pandas as pd
# df = pd.read_csv(r'archive (1)\Titanic-Dataset.csv')
# df['Age'] = df['Age'].fillna(df['Age'].mean())
# print(df)


# 5. Fill missing values in Embarked with the most frequent port (mode)
# import pandas as pd
# df = pd.read_csv(r'archive (1)\Titanic-Dataset.csv')
# df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])
# print(df)


# 6. Check that there are no missing values left in Age and Embarked.
# import pandas as pd
# df = pd.read_csv(r'archive (1)\Titanic-Dataset.csv')
# df[['Age', 'Embarked']].isna().sum()
# print(df)


#7. Remove duplicate rows if any
# import pandas as pd
# df = pd.read_csv(r'archive (1)\Titanic-Dataset.csv')
# df.drop_duplicates(inplace=True)
# print(df)



# SECTION C — DATA MANIPULATION:-

# 1. Convert the Sex column into numeric format (male → 0, female → 1)
# import pandas as pd
# df = pd.read_csv(r'archive (1)\Titanic-Dataset.csv')
# df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})
# print(df)


# 2. Convert the Embarked column to a categorical datatype
# import pandas as pd
# df = pd.read_csv(r'archive (1)\Titanic-Dataset.csv')
# df['Embarked'] = df['Embarked'].astype('category')
# print(df)


# 3. Create a new column FamilySize = SibSp + Parch + 1
# import pandas as pd
# df = pd.read_csv(r'archive (1)\Titanic-Dataset.csv')
# df['FamilySize'] = df['SibSp'] + df['Parch'] + 1
# print(df)


# 4. Create a new column IsAlone where 1 indicates the passenger is alone (FamilySize == 1), else 0.
# import pandas as pd
# df = pd.read_csv(r'archive (1)\Titanic-Dataset.csv')
# df['IsAlone'] = (df['FamilySize'] == 1).astype(int)
# print(df)


# 5. Rename the column Pclass to PassengerClass.
# import pandas as pd
# df = pd.read_csv(r'archive (1)\Titanic-Dataset.csv')
# df.rename(columns={'Pclass': 'PassengerClass'}, inplace=True)
# print(df)


# 6. Convert Fare to integer values.
# import pandas as pd
# df = pd.read_csv(r'archive (1)\Titanic-Dataset.csv')
# df['Fare'] = df['Fare'].astype(int)
# print(df)


# SECTION D — FILTERING & SELECTION:-

# 1. Filter and display all passengers who survived (Survived == 1).
# import pandas as pd
# df = pd.read_csv(r'archive (1)\Titanic-Dataset.csv')
# df[df['Survived'] == 1]
# print(df)


# 2. Get passengers who are in 1st class (PassengerClass == 1)
# import pandas as pd
# df = pd.read_csv(r'archive (1)\Titanic-Dataset.csv')
# df[df['PassengerClass'] == 1]
# print(df)


# 3. Filter passengers whose age is greater than 50.
# import pandas as pd
# df = pd.read_csv(r'archive (1)\Titanic-Dataset.csv')
# df[df['Age'] > 50]
# print(df)


# 4. Filter female passengers who survived
# import pandas as pd
# df = pd.read_csv(r'archive (1)\Titanic-Dataset.csv')
# df[(df['Sex'] == 1) & (df['Survived'] == 1)]
# print(df)


# 5. Select passengers who paid a fare above the average fare
# import pandas as pd
# df = pd.read_csv(r'archive (1)\Titanic-Dataset.csv')
# df[df['Fare'] > df['Fare'].mean()]
# print(df)


# 6. Select only columns: Name, Sex, Age, Survived.
# import pandas as pd
# df = pd.read_csv(r'archive (1)\Titanic-Dataset.csv')
# df[['Name', 'Sex', 'Age', 'Survived']]
# print(df)


#7. Using loc, select rows from index 100 to index 150 (inclusive)
# import pandas as pd
# df = pd.read_csv(r'archive (1)\Titanic-Dataset.csv')
# df.loc[100:150]
# print(df)

# 8. Using iloc, select the first 10 rows and first 6 columns
# import pandas as pd
# df = pd.read_csv(r'archive (1)\Titanic-Dataset.csv')
# df.iloc[:10, :6]
# print(df)


# SECTION E — SORTING & AGGREGATION:-

# 1. Sort passengers by Fare in descending order
# import pandas as pd
# df = pd.read_csv(r'archive (1)\Titanic-Dataset.csv')
# df_sorted_fare = df.sort_values(by='Fare', ascending=False)
# print(df_sorted_fare)


# 2. Sort passengers first by PassengerClass, then by Fare descending
# import pandas as pd
# df = pd.read_csv(r'archive (1)\Titanic-Dataset.csv')
# df_sorted_class_fare = df.sort_values(by=['PassengerClass', 'Fare'], ascending=[True, False])
# print(df_sorted_class_fare)


# 3. Find the average age of passengers
# import pandas as pd
# df = pd.read_csv(r'archive (1)\Titanic-Dataset.csv')
# average_age = df['Age'].mean()
# print(average_age)


# 4. Compute the average fare paid by each passenger class
# import pandas as pd
# df = pd.read_csv(r'archive (1)\Titanic-Dataset.csv')
# average_fare_by_class = df.groupby('PassengerClass')['Fare'].mean()
# print(average_fare_by_class)


# 5. Count the number of passengers in each embarkation port
# import pandas as pd
# df = pd.read_csv(r'archive (1)\Titanic-Dataset.csv')
# passengers_by_port = df['Embarked'].value_counts()
# print(passengers_by_port)


# 6. Count how many male and female passengers there are
# import pandas as pd
# df = pd.read_csv(r'archive (1)\Titanic-Dataset.csv')
# passengers_by_sex = df['Sex'].value_counts()
# print(passengers_by_sex)


# SECTION F — GROUPBY & APPLY:-

# 2. Find the survival rate by gender.
# import pandas as pd
# df = pd.read_csv(r'archive (1)\Titanic-Dataset.csv')
# survival_by_gender = df.groupby('Sex')['Survived'].mean()
# print(survival_by_gender)


# 3. Use apply() to create a new column AgeGroup
# import pandas as pd
# df = pd.read_csv(r'archive (1)\Titanic-Dataset.csv')
# def age_group(age):
#     if age < 12:
#         return 'Child'
#     elif age < 60:
#         return 'Adult'
#     else:
#         return 'Senior'

# df['AgeGroup'] = df['Age'].apply(age_group)




# SECTION G — ANALYSIS & EXPORT:-
# 1. Identify the passenger(s) who paid the highest fare
# import pandas as pd
# df = pd.read_csv(r'archive (1)\Titanic-Dataset.csv')
# max_fare = df['Fare'].max()
# highest_payers = df[df['Fare'] == max_fare]
# print(highest_payers)


# 2. Find which embarkation port has the highest number of passengers
# import pandas as pd
# df = pd.read_csv(r'archive (1)\Titanic-Dataset.csv')
# print(df.groupby("Embarked")["PassengerId"].count().max())


# 3. Compare survival rate between passengers who were alone vs those with family.
