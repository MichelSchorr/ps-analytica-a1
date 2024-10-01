import pandas as pd

list = [1,2,3,4,5]
series = pd.Series(list)

print(series.std())

df = pd.DataFrame({
    "col1": [1,2,3,4],
    "col2":  ["a","b","c","d"],
    "col3": [5.3, 3.2, 5.0, 4.5]
})


print(df)
print(df.loc[1:3, "col1":"col3" ])


filtro =  df["col1"] == 2
df_filtrado = df[~filtro]

print(df_filtrado)