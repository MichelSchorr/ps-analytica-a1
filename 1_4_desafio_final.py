import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('Dataset_Processo_Seletivo_UFRJ_Analytica_2024-2.csv')




expc_vida_1991 = df[df["ano"] == 1991]["expectativa_vida"]
expc_vida_2010 = df[df["ano"] == 2010]["expectativa_vida"]




#diferenca na expectativa de vida
dif_expc_vida_num = []
for x in range(expc_vida_1991.size):
    dif_expc_vida_num.append(expc_vida_2010[x+54]-expc_vida_1991[x])



dif_expc_vida = pd.DataFrame({
    "sigla_uf": ["AC", "AL", "AM","AP", "BA", "CE", "DF", "ES", "GO", "MA", "MG", "MS", "MT", "PA", "PB", "PE", "PI", "PR", "RJ", "RN", "RO", "RR", "RS", "SC", "SE", "SP", "TO"],
    "mud_expec_vida": dif_expc_vida_num
})


#filtragem para diferencas maiores que 10
dif_expc_vida_m_10 = dif_expc_vida[dif_expc_vida["mud_expec_vida"] >= 10]




plt.bar(dif_expc_vida_m_10["sigla_uf"], dif_expc_vida_m_10["mud_expec_vida"])
plt.show()

print(dif_expc_vida)
