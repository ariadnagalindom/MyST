import pandas as pd 
import matplotlib.pyplot as plt
import os 
import sys 
import glob
import pandas_datareader.data as web
from functions import get_adj_closes


#cedir = os.path.dirname(os.path.abspath(sys.argv[0]))
#print(cedir)

# Definir capital, comision y tasa libre de riesgo.
capital = 1000000
comision = 0.00125
rf = 0.0429
 
# Obtenemos un DataFrame con las fechas y las ordenamos.
fechas = []

# Conseguimos los nombres de los archivos 
#for files in glob.glob(cedir + '/MyST/files/*.csv'): #iOs
for files in glob.glob( 'C:\\Users\\ariad\\OneDrive\\Documentos\\GitHub\\MyST\\files\\*.csv'): #Windows
    fechas.append(files[-12:-8] + files[-8:-6] + files[-6:-4])

# Conseguimos los directorios completos de los archivos a leer 
#dates = [cedir + '/MyST/files/NAFTRAC_' + fechas[i] + '.csv' for i in range(0, len(fechas))] #iOs
dates = [ 'C:\\Users\\ariad\\OneDrive\\Documentos\\GitHub\\MyST\\files\\NAFTRAC_' + fechas[i] + '.csv' for i in range(0, len(fechas))] #Windows

# Leemos todos los archivos 
dataframes = [pd.read_csv(i, skiprows=2) for i in dates]
# Eliminamos NaN
dataframes = [dataframes[i].dropna().replace(',', '', regex=True) for i in range(0, len(dataframes))]
#print(dataframes)
# Sacamos los tickers 
tickers = dataframes[0].loc[:,"Ticker"].reset_index(drop = True)
# Agregamos el .MX a los tickers
tickers = [tickers[i] + ".MX" for i in range(0, len(tickers))]
# Eliminamos los * de los tickers
tickers = [tickers[i].replace("*", "") for i in range(0, len(tickers))]
#print(tickers)

# Cambiamos los tickers erroneos
i = 0
while i <= len(tickers)-1:
    if tickers[i] == 'LIVEPOLC.1.MX':
        tickers[i] = 'LIVEPOLC-1.MX'
        i = i+1

    elif tickers[i] =='MEXCHEM.MX':
        tickers[i] = 'ORBIA.MX'
        i = i+1

    elif tickers[i] == 'GFREGIOO.MX':
        tickers[i] = 'RA.MX'
        i = i+1

    else:
        tickers[i] = tickers[i]
        i = i+1



#print(tickers)

# Sacamos lo que designamos como cash 
tickers.remove("MXN.MX")
tickers.remove("KOFL.MX")

# Obtenemos precios mensuales
precios_mensuales = pd.DataFrame(get_adj_closes(tickers=tickers, start_date="2018-01-01", end_date="2021-01-31"))

# Agrupamos los precios por mes 
precios_mensuales = precios_mensuales.groupby(pd.Grouper(freq="M")).last()

precios_ipc = pd.DataFrame(get_adj_closes(tickers=["^MXX"], start_date="2018-01-01", end_date="2021-01-31"))
precios_ipc = precios_ipc.groupby(pd.Grouper(freq="M")).last()

## inversión ACTIVA
# Obtenemos precios diarios 
precios_diarios = pd.DataFrame(get_adj_closes(tickers = tickers, start_date="2018-01-31", end_date="2021-01-31"))



