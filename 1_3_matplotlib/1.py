import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('Dataset_Processo_Seletivo_UFRJ_Analytica_2024-2.csv')
df_1991 = df[ df["ano"]==1991]

estados = df_1991.sort_values(by="populacao_urbana", ascending=False)["sigla_uf"]
pop_urb = df_1991.sort_values(by="populacao_urbana", ascending=False)["populacao_urbana"]

plt.bar(estados, pop_urb)
plt.show()