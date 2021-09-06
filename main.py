from numpy.testing._private.utils import print_assert_equal
import pandas as pd
import numpy as np
from pandas.core.frame import DataFrame
import yfinance as yf
from datetime import datetime
from os import path
import os 
import xlrd
import sys 
import glob
import pandas_datareader.data as web
import matplotlib.pyplot as plt


cedir = os.path.dirname(os.path.abspath(sys.argv[0]))
print(cedir)

# Definir capital, comision y tasa libre de riesgo.
capital = 1000000
comision = 0.00125
rf = 0.0429
 
# Obtenemos un DataFrame con las fechas y las ordenamos.
fechas = []

for files in glob.glob(cedir + '/brunopimentel/Documents/GitHub/MyST/files/*.csv'):
    fechas.append(files[-12:-8] + '/' + files[-8:-6] + '/' + files[-6:-4])

fcd = pd.DataFrame()

fcd['Date'] = fechas 
fcd['Date'] = pd.to_datetime(fcd['Date'], format='%Y-%m-%d')

dates = list(fcd['Date'])

fcd = fcd.sort_values(["Date"])

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

# Función para descargar precios de cierre ajustados:
def get_adj_closes(tickers, start_date=None, end_date=None, freq='m'):
    # Fecha inicio por defecto (start_date='2010-01-01') y fecha fin por defecto (end_date=today)
    # Descargamos DataFrame con todos los datos
    closes = yf.download(tickers=list(ticker), start='2019-01-01', end='2019-12-31', progress=False)
    # Se ordenan los índices de manera ascendente
    #closes.sort_index(inplace=True)
    #return closes

#YahooDailyReader

data_prices = yf.download(tickers=ticker2, start=dates, end='2019-12-31', progress=False)

data_prices = data_prices.iloc[:, 0:35]
print(data_prices)

