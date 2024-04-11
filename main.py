# AttributeError: Can only use .str accessor with string values

import pandas as pd

df = pd.DataFrame({
    'name': ['Alice', 'Bobby', 'Carl', 'Dan'],
    'experience': [1, 3, 5, 7],
    'salary': [175.1, 180.2, 190.3, 205.4],
})

# 0    Alice
# 1      Tom
# 2     Carl
# 3      Dan
# Name: name, dtype: object
print(df['name'].str.replace('Bobby', 'Tom'))
