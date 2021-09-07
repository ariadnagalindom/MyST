# Descargarmos librerias 
from numpy.lib.function_base import append
from numpy.testing._private.utils import print_assert_equal
import pandas as pd
import numpy as np
from pandas.core.frame import DataFrame
import yfinance as yf
from datetime import date, datetime
from os import cpu_count, path
import os 
import xlrd
import sys 
import glob
import pandas_datareader.data as web
import matplotlib.pyplot as plt
from datetime import timedelta

cedir = os.path.dirname(os.path.abspath(sys.argv[0]))
print(cedir)

# Definir capital, comision y tasa libre de riesgo.
capital = 1000000
comision = 0.00125
rf = 0.0429
 
# Obtenemos un DataFrame con las fechas y las ordenamos.
fechas = []

for files in glob.glob(cedir + '/brunopimentel/Documents/GitHub/MyST/files/*.csv'):
    fechas.append(files[-12:-8] + files[-8:-6] + files[-6:-4])

print(fechas)

fcd = pd.DataFrame()

fcd['Date'] = fechas 

dates = list(fcd['Date'])
print(dates)
print(len(dates))

g = []
i = 0

while i <= 40:
    fechas = pd.to_datetime(dates[i], format='%Y/%m/%d')
    g.append(fechas)
    i = i + 1

a = DataFrame()
a['Date'] = g
a = a.sort_values(['Date'])
a = a.reset_index()
print(a['Date'])

# Obtenemos los tickers y los pesos.
data = pd.read_csv(cedir + '/brunopimentel/Documents/GitHub/MyST/files//NAFTRAC_20180131.csv', skiprows=2)

ticker  = list(data.T.iloc[0])
ticker = pd.DataFrame(ticker)

ticker = ticker.replace('\*','',regex=True).astype(str)
ticker = ticker.replace('LIVEPOLC.1', 'LIVEPOLC-1')
ticker = ticker.replace('MEXCHEM', 'ORBIA')
ticker = ticker.replace('GFREGIOO', 'RA')
ticker = ticker[0] + '.MX'
ticker2 = list(ticker[0:])

print(ticker2)
weight  = data.T.iloc[3]

print(len(a['Date']))

# Descargamos precios 
k = 0
price = []

while k <= len(a['Date']):
    start = a['Date'][k]
    data_prices = yf.download(tickers=ticker2, start=start, end=start + timedelta(days=1), progress=False)
    price.append(data_prices)
    k = k+1

price = price.iloc[:, 0:35]
print(price)

datos_fi  = pd.DataFrame()
datos_fi = price

print((datos_fi))

lista = pd.DataFrame()



capital  = capital - (capital * comision)
lista['tikckers'] = ticker2
lista['pesos'] = weight/100
lista['cap_x_ticker'] = capital * lista['pesos']
lista['titulos'] = lista['cap_x_ticker'] / 

print(datos_fi[0:10])

print(lista)

x = sum(lista['titulos'])
print(x)

titulos * precio * comision  = capital 

precio capital / comision /














a['Date'][0]

start = a['Date'][0]

data_prices = yf.download(tickers=ticker2, start=start, end=start + timedelta(days=1), progress=False)

m = 0

for m in range(40):
    data_prices = yf.download(tickers=ticker2, start=a['Date'][i], end='2019-12-31', progress=False)

fu = pd.DataFrame()

dati2 = pd.DataFrame()
k = 0
while k <= len(a['Date']):
    dati = yf.download(tickers=ticker2[k], start=start, end = start + timedelta(days=1), progress=False)
    #dati2 = dati['Adj Close']
    k = k+1

dati = yf.download(tickers=ticker2[k], start=start, end = start + timedelta(days=1), progress=False)
dati2 = dati['Adj Close']
print(dati)
print(dati2)