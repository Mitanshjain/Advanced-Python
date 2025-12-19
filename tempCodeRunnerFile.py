import pandas as pd
df = pd.read_csv("StudentsPerformance.csv")
print(df[(df['writing score']<50)])