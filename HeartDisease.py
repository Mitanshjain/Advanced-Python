import pandas as pd
df = pd.read_csv(r"C:\Users\MY PC\OneDrive\Desktop\Advance Python by vinay sir\archive (2)\Heart_Disease_Prediction.csv")
# print(df)
# print(df.head()) # To print first five rows
# print(df.sample()) # it gives one row which are random

# print(df.sample(10)) # It gives random 10 rows

# print(df.columns) # It gives columns in data sheet
# print(df['Age']) # It gives age column

# print(df['Age'].dtype) # It gives data type

# print(df['Age'].astype('float')) # Astype is used to change the datatype of the perticular column , .astype('data type)

# df['Age'] = (df['Age'].astype('float'))
# print(df['Age'])
# print(df['Age'].dtype) # for converting integer to float


# print(df['FBS over 120'])
# print(df['FBS over 120'].value_counts())  # To check how many zeros and ones in FBS over 120

# How to check categorical and numerical idenftify

# print(df.info()) # to get information of which type of datatype we have

# cat_col = df.select_dtypes(include='object').columns
# print(cat_col)                                     # it gives object type of data type

# cat_col = df.select_dtypes(exclude='object').columns
# print(cat_col)                                     # It gives data exclude than object type


# max_Age = df['Age'].max()
# min_Age = df['Age'].min()
# print("Max age :",max_Age) # It gives specific what we demand
# print("Min age:", min_Age) # It gives specific what we demand 


# print(df.describe()) # Both gives max min mean and all





