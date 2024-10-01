import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('Dataset_Processo_Seletivo_UFRJ_Analytica_2024-2.csv')


plt.scatter(df["idhm"], df["expectativa_vida"])
plt.show()