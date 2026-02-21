import sys
sys.path.append('/home/tirilero/Desktop/Codigos/python_functions')
import vic_plot
import pandas as pd
from io import StringIO
from sklearn.linear_model import LinearRegression
import datetime
import numpy as np
"""
coefficients = np.polyfit(x_data, y_data, 3)
poly = np.poly1d(coefficients)
fit_data=poly(x_data)

a, b, c, d = coefficients
"""

"""
Primer trabajo,Counter,Nombre
2024-01,1,Mauricio Aguilera
2024-12,3,Isidora Olivares
2024-12,3,Daniel Rivera
2025-02,4,Ignacio Pizarro
2025-04,5,Camila Zamorano
2025-07,7,Alar Hurqueta
2025-07,7,Gonzalo Espinoza
2025-09,8,Juan Carmona
2025-10,10,Jorge Vargas
2025-10,10,Matías Carrión
,,Soledad Plaza
,,Luis Riveros 
,,Julian Gonzalez
,,Antonia Traslaviña 
,,Luis Santa María
,,Sebastian Lagunas
,,Vicente González
,,Jorge Alfaro
"""
data_str="""
Date,Counter,Nombre
2024-01,1,Mauricio Aguilera
2024-12,3,Isidora Olivares
2024-12,3,Daniel Rivera
2025-02,4,Ignacio Pizarro
2025-04,5,Camila Zamorano
2025-07,7,Alar Hurqueta
2025-07,7,Gonzalo Espinoza
2025-09,8,Juan Carmona
2025-10,10,Matias Carrion
2025-10,10,Jorge Vargas
"""
df = pd.read_csv(StringIO(data_str),comment="#")
df["Counter"]=df["Counter"]/18

df2 = pd.DataFrame(data={
    "Date":["2025-03","2026-11","2026-12"]
    })

df["Date"]=pd.to_datetime(df["Date"], format="%Y-%m")
df["Date_int"]=df['Date'].astype(int)

"""
model = LinearRegression()
model.fit(df[["Date_int"]], df["Counter"])
print(f"Slope: {model.coef_[0]}")
print(f"Intercept: {model.intercept_}")
exit()
"""

Slope=1.3051473165433279e-17
Intercept= -22.47068913991991

#Slope= 1.5697349428936418e-17
#Intercept= -27.032454854085305


df2["Date"]=pd.to_datetime(df2["Date"], format="%Y-%m")
df2["Date_int"]=df2['Date'].astype(int)
df2["Predict"]=df2["Date_int"]*Slope+Intercept

fig,ax=vic_plot.config(
        title="Seguimiento de empleabilidad titulados 2025-03",
        x_label="Fecha",
        y_label="Trabajadores/18"
        )

import matplotlib.pyplot as plt
plt.rcParams.update({
          'figure.subplot.bottom'   :   16/15*5/6,
          'grid.color'              : '#ff5200',
          'grid.linewidth'          : 0.8
        })


ax.plot(df["Date"],df["Counter"],label="Primer trabajo")
ax.plot(df2["Date"],df2["Predict"],label="Predicción",linestyle="--",linewidth=1)
ax.set_ylim([0,1])
ax.tick_params(axis='x', rotation=90)

vic_plot.savefig(fig,"lol.png")

