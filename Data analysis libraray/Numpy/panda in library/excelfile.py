import pandas as pd

data=pd.read_excel(
    "C:/Users/brobu/OneDrive/Documents/Python/converting to excel.xlsx"
)

print(f"the data of excel file : \n {data}")

print(f"the data has {len(data)} rows and {len(data.columns)} columns.\n")

information_of_data =data.info()
print("information of data : \n",information_of_data)

print(data["cloud"].describe())

#the notna() conditional function returns a true fro each row the values are not a null value

#it is used to remove or filter out missing (Nan) values in a panda dataframe


cloud_no_na = data[data["cloud"].notna()]
print(cloud_no_na)


#filter the only github cloud

githubcloud= data.loc[data["cloud"] =="GitHub"]
print("\nOnly Github Cloud :\n", githubcloud, "\n ")


amazoncloud= data.loc[data["cloud"] =="Amazon"]
print("\nOnly Github Cloud :\n", amazoncloud, "\n ")