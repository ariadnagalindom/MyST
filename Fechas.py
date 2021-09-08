# Descargarmos librerias 
from numpy.lib.arraysetops import isin
from numpy.lib.function_base import append
from numpy.testing._private.utils import print_assert_equal
import pandas as pd
import numpy as np
from pandas.core.frame import DataFrame
from pandas.core.indexes.period import period_range
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

for files in glob.glob(cedir + '/MyST/files/*.csv'):
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
data = pd.read_csv(cedir + '/MyST/files//NAFTRAC_20180131.csv', skiprows=2)

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
start = a['Date'][0]
data_prices = yf.download(tickers=ticker2, start=start, end=a['Date'].iloc[-1], progress=False, interval='1d')
price = data_prices['Close']
print(price)

# Valuación 

precios_ini = list(price.iloc[0,:])
print(precios_ini)
lista = pd.DataFrame()

capital  = capital - (capital * comision)
lista['tikckers'] = ticker2
lista['pesos'] = weight/100
lista['cap_x_ticker'] = capital * lista['pesos']
lista['Precios_ini'] = precios_ini
lista['titulos'] = lista['cap_x_ticker'] / lista['Precios_ini']










print(lista)
x = []
for dates in (a['Date']):
    xa = price.loc[dates]
    xa.append(xa)


price['fechas'] = price.index
print(price)
print(price['fechas'].iloc[1])




lista['precio'] = 0

for i in range(38):
    if price['fechas'].iloc[i] == a['Date'][i]:
        lista['precio' + i].iloc[i] = price.iloc[i,i:]
print(lista)



for i in range(37):
    if price['fechas'].iloc[i] == a['Date'][i]:
        lista.append[price.iloc[i,i:]]
print(lista)

print(price['fechas'].iloc[0])
print(a['Date'][0])
print(price.iloc[0,0:])



x = []
for dates in (a['Date']):
    xa['price'] = price.loc[dates]
    xa.append(xa)










xa['MEGACPO.MX']


price.get('Date')

price.to_frame()
price['Date'] = a['Date']
print(price['Date'])

final = pd.DataFrame()
final['Fecha'] = a['Date']

print(list(price['Date']))

m = 0
while m <= 40:
    if (price['Date']) in list(a['Date']):
        final['Capital'] = price.iloc[i]
        m = m+1

print(final['Capital'])

print(price.iloc[0])







x = price.sum(price)

ps = pd.DataFrame()
ps = price
print(price)
print(a['Date'])



final = pd.DataFrame()
final['Fecha'] = a['Date']

for price.index in a['Date']:
    final['capital'] = lista['titulos'] * price[i]
    print(final)





final['capital'] = sum(lista['titulos'] * lista['Precios_ini'])

print(sum(lista['titulos'] * lista['Precios_ini']))

print(ticker2)
print(a['Date'])













