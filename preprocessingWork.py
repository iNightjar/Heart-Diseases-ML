import pandas as pd

dataframe = pd.read_csv('heart_disease_data.csv')

# print(dataframe.shape)    # num of columns
# print(dataframe.dtypes)   # print datatypes
# print(dataframe.describe()) # simple description of the dataset
# print(dataframe.loc[1]) # print elements with values, like working with arrays..

# print(dataframe.iloc[2:5]) # range to call


range = dataframe.loc[:, 'age']

cleaned_age = []

# print(list(range.mode())[0])

for iterator in range:
    if str(iterator).endswith("0") or str(iterator).endswith("1"):
        cleaned_age.append(str(iterator))

    else:
        cleaned_age.append(range.mode())


# print(cleaned_age)
