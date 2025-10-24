#!/bin/python3
import pandas as pd

chanceData = pd.read_csv("admission_chances.csv")
scoresData = pd.read_csv("admission_scores.csv")

# convert to dataframe

def pandas_df_transform(df: pd.DataFrame) -> pd.DataFrame:

    if df is None or df.empty:
        print ("No data to display")
        return pd.DataFrame()

    for col in df.columns:
        df[col] = pd.to_numeric(df[col], errors="ignore")

    df = df.sort_index(ascending=True)

    pd.set_option("display.max_rows", None)
    pd.set_option("display.max_columns", None)

    return df

Dataframe_ch = pandas_df_transform(chanceData)
Dataframe_sc = pandas_df_transform(scoresData)

# pick a column that appears in both dataframes e.g. Serial_Number

KEY = "Serial_Number"

# merged dataframes

merged_data = Dataframe_ch.merge(
    Dataframe_sc,
    on=KEY,
    how="inner",  # can pick -> inner | left | right | outer
    suffixes=("_chance", "_score")
)

#clean the data by removing rows with missing data

cleaned_data = merged_data.dropna()




# print dataframes

#print(Dataframe_ch)
#print(Dataframe_sc)

# print merged data

#print(merged_data)

# print clean merge

print(cleaned_data)
cleaned_data.to_csv('admission_cleaned_joined.csv', index=False)