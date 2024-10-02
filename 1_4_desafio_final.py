import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('Dataset_Processo_Seletivo_UFRJ_Analytica_2024-2.csv')




#diferenca na expectativa de vida de 1991 para 2010 em cada uf
dif_expc_vida_num = []
for x in df[df["ano"] == 1991]["sigla_uf"]:
    dif_expc_vida_num.append(df[(df["ano"] == 2010) & (df["sigla_uf"] == x)]["expectativa_vida"].values[0] - df[(df["ano"] == 1991) & (df["sigla_uf"] == x)]["expectativa_vida"].values[0])



#tabela com expectativas de vida em 1991, 2010, e mudanca entre os anos
mudanca_expec_vida = pd.DataFrame({
    "sigla_uf": df[df["ano"] == 1991]["sigla_uf"].values[:],
    "expectativa_vida_1991": df[df["ano"] == 1991]["expectativa_vida"].values[:],
    "expectativa_vida_2010": df[df["ano"] == 2010]["expectativa_vida"].values[:],
    "dif_expectativa_vida": dif_expc_vida_num
})



#filtragem para diferencas maiores que 10
mudanca_expec_vida = mudanca_expec_vida[mudanca_expec_vida["dif_expectativa_vida"] >= 10]



plt.bar(mudanca_expec_vida["sigla_uf"], mudanca_expec_vida["dif_expectativa_vida"])
plt.show()