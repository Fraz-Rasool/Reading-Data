import pandas as pd
import numpy as np

dataSet={
    'Id':[1,2,3,np.nan,5],
    'Name':["Fraz","Hasan","Umar","Mohsin","Umais"],
    'Salary':[90000,np.nan,450000,np.nan,80000],
    'Age':[19,21,np.nan,25,np.nan],
    'Department':['AI','AI',np.nan,'CS','CS']
}

df = pd.DataFrame(dataSet)
print(df)

print("\n")

df['Age'].fillna(df['Age'].median(),inplace=True)
# print(f"After Age Median Imputation:\n{df}")

df['Salary'].fillna(df['Salary'].mean(),inplace=True)
# print(f"After Salary Mean Imputation:\n{df}")

df['Department'].fillna(df['Department'].mode()[0],inplace=True)
# print(f"After Department Mode Imputation:\n{df}")

df["Id"].interpolate(method='linear',inplace=True)
print(f"After Id Interpolation:\n{df}")

# Same as for forward fill and backward fill using method ='ffill' or 'bfill'