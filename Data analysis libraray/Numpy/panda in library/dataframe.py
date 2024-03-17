import pandas as pd

data =pd.DataFrame(
    {
        "name": ["Hare","Krishna", "Hare","Ram"],
        "age": [100,200,100,300],
        "gender" :["mantra","male","mantra","male"],
    }
)

print("The Datframe is: \n",data)

print("age\n ",data["age"])

gender=pd.Series(["mantra","male","mantra","male"],name="gender")
print(f"the series of age is: \n {gender}")

age=pd.Series(data["age"])
print(f"series of age \n {age}")


max_age = data["age"].max()
print(f"The maximum age is :\n :{max_age}")


##discribe()

describe =data.describe()
print(f"Describe the details of data : \n{describe}")