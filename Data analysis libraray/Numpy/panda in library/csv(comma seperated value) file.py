import pandas as pd

data=pd.read_csv(
    "C:/Users/brobu/OneDrive/Documents/Python/Data analysis libraray/Numpy/panda in library/datasets.csv"

)

print(f"the data of csv :\n {data}")

head=data.head(10)
print(f"the head to elements of csv file :\n {head} ")

tail=data.tail(4)
print(f"the tail elements of csv file :\n{tail}\n")

#print the data types of the dataframe
print(data.dtypes)

#writing dataframe to a csv file

data.to_csv("sample_datasets.csv", index = False)

#writing dataframe to a excel file

data.to_excel("converting to excel.xlsx",sheet_name="sheet1")