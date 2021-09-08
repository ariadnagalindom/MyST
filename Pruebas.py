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


