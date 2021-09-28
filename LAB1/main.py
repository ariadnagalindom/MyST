# Descargamos liberías y data
from data import dataframes
from data import precios_mensuales
from data import capital
from data import comision
from data import rf
import math as m
from data import precios_diarios
import pandas as pd
from sympy.solvers import solve
from sympy import Symbol

# Importamos los pirmeros datos 
datos = dataframes[0].drop([10, 35]).reset_index(drop=True)

# Obtenemos los pesos de nuestros tickers 
weigths = datos["Peso (%)"] / 100

# Sacamos las ponderaciones de nuetro dinero por ticker 
wei_x_tic = capital * weigths

# Obtenemos los precios por ticker 
din_x_tic = precios_mensuales.iloc[0, :]

# Cantidad de titulos a comprar por ticker
cant_titulos = [wei_x_tic[i] / din_x_tic[i] for i in range(0, len(wei_x_tic))]

# Se redondean las cantidad de titulos 
cant_titulos = [m.trunc(cant_titulos[i]) for i in range(0, len(wei_x_tic))]

# Obtenemos las comisiones totales por la compra de titulos 
com_total = sum(cant_titulos * din_x_tic * comision)

# Sacamos nuestra cantidad de efectivo
efectivo = capital - sum(cant_titulos * din_x_tic) - com_total

# Obtenemos el valor del portafolio incial 
v_port_ini = sum(cant_titulos * din_x_tic) + efectivo

# Obtenemos los valores del portafolio en el tiempo
v_port_pas = [sum(precios_mensuales.iloc[i, :] * cant_titulos) for i in range(1, len(precios_mensuales))]

# Insertamos el valor del portafolio incial
v_port_pas.insert(0, v_port_ini)


### Activa 

# Pesos en porcentaje
weigths = dataframes[0].drop([10, 35], axis=0).reset_index(drop=True)["Peso (%)"]/100

# Cantidad de capital por peso
wei_x_tic = (capital * weigths).to_list()

# Cantidad que invertiremos por ticker
din_x_tic = precios_diarios.iloc[0 , :]

# Cantidad de titulos
cant_titulos = [wei_x_tic[i]/din_x_tic[i] for i in range(0, len(weigths))]

# Redondeo de la cantidad de titulos
cant_titulos = [m.floor(cant_titulos[i]) for i in range(0, len(wei_x_tic))]

# Creación del DataFrame con nuestras fechas y nuestros tickers
titulos_fecha = pd.DataFrame(columns=precios_diarios.columns, index=precios_diarios.index)

# Llenado de DataFrame con los precios de nuestors tickers en el tiempo
for i in range(0, len(precios_diarios.index)):
    titulos_fecha.iloc[i] = cant_titulos

# Obtenemos el rendimiento de nuestro portafolio en el tiempo 
rendimietno = precios_diarios.iloc[:, :-1].pct_change().dropna() #hasta aqui funciona

fechas_con_bajadas = rendimietno[rendimietno >= -.05]

fechas_con_subidas = rendimietno[rendimietno >= .05]

print(fechas_con_bajadas)

x = pd.DataFrame()
for i in range(0,len(rendimietno.index)):
    if rendimietno[i] >= 0.05:
        x[i] = cant_titulos[i] * 0.025
    if rendimietno[i] <= -0.05:
        x[i] = cant_titulos[i] * 0.025

print(x)