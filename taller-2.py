# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 10:49:51 2022

@author: k-ami
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ruta="C:/Users/k-ami/OneDrive/Documentos/tadeo/2022-1/aprendizaje"


fasecolda = ruta + "/guia_fasecolda.csv"

df1 = pd.read_csv(fasecolda)

filtro=df1[(df1["Marca"]=="AUTECO") | (df1["Marca"]=="Asia") & (df1["Novedad"]=="M")]
df4=pd.DataFrame(data= filtro)

df4.to_csv(ruta + "/guia_fasecolda.csv",index=True)

print(df4.columns)
df1.describe()

df4.groupby("Marca")["Peso"].sum().plot(kind="bar")
df4.groupby("Marca")["Peso"].sum().plot(kind="line")
df4.groupby("Marca")["Peso"].sum().plot(kind="hist",legend="reverse")
df4.groupby("Marca")["Peso"].count().plot(kind="barh",legend="reverse")

df4.Marca.groupby(df1.Marca).count().plot(kind="pie")
plt.axls("equal")