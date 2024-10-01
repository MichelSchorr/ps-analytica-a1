import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('Dataset_Processo_Seletivo_UFRJ_Analytica_2024-2.csv')
df_1991 = df[ df["ano"]==1991]
df_2000 = df[ df["ano"]==2000]
df_2010 = df[ df["ano"]==2010]


plt.hist(df_1991["idhm"])
plt.show()


plt.hist(df_2000["idhm"])
plt.show()


plt.hist(df_2010["idhm"])
plt.show()
