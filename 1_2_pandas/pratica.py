import pandas as pd

df = pd.read_csv('Dataset_Processo_Seletivo_UFRJ_Analytica_2024-2.csv')




#3
df_1991 = df[ df["ano"]==1991]

idh_1991 = df_1991.loc[:, "idhm"]

print("3) media idh 1991: ", idh_1991.mean())
print()



#4
df_filtrado = df_1991[df_1991["idhm"]>idh_1991.mean()]

print("4) estados com idh acima da media em 1991: ")
print(df_filtrado)
print()


#5
print("5) estados ordenados por idh em 1991: ")
df_sorted = df_1991.sort_values(by="idhm")
print(df_sorted.head(5))
print()


#6
print("6)")
print("estado de maior idh: ", df_1991.loc[df_1991["idhm"].idxmax(), "sigla_uf"], df_1991["idhm"].max())