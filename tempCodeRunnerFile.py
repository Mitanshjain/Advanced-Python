import pandas as pd
d = {
    'a':10,
    'b':20,
    'c':30,
    'd':40
}
s1 = pd.Series(d)
print(s1.values)