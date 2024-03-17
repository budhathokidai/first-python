import pandas as pd

data=pd.read_csv(
    "C:/Users/brobu/OneDrive/Documents/Python/Data analysis libraray/Numpy/panda in library/datasets.csv"
)


#writing dataframe to a excel file

data.to_excel("converting to excel.xlsx",sheet_name="sheet1")