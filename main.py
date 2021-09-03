import pandas as pd
import numpy as np
import yfinance as yf
from datetime import datetime
from os import path
import os 
import xlrd
import sys 
import glob

cedir = os.path.dirname(os.path.abspath(sys.argv[0]))

# Definir capital, comision y tasa libre de riesgo.
capital = 1000000
comision = 0.00125
rf = 0.0429
abspath= path.abspath(cedir + '/MyST/files/NAFTRAC_20180131.csv')
archivos = [f[8:-4] for f in os.listdir(abspath) if isfile(join(abspath, f))]
archivos = ['NAFTRAC_'+ i.strftime('%d%m%y') for i in sorted(pd.to_datetime(files))]
datos = {} # Llaves para indicar que es diccionario
for i in archivos:
    data = pd.read_csv('Usuarios/brunopimentel/Documentos/GitHub/MyST/files/NAFTRAC_2018_2021/NAFTRAC_2018_2021/' + i + '.csv',
                       skiprows=2, usecols=['Ticker', 'Peso (%)']).dropna()
    dicti = {'Ticker': str, 'Peso (%)': float}
    data = data.astype(dicti)
    data['Ticker'] = [i.replace('*', '') for i in data['Ticker']]
    data['Ticker'] = data['Ticker'] + '.MX'
    data['Ticker'] = [i.replace('LIVEPOLC.1.MX', 'LIVEPOLC-1.MX') for i in data['Ticker']]
    data['Peso (%)'] = data['Peso (%)'] / 100
    datos[i] = data



for files in glob.glob(cedir + '/MyST/files/*.csv'):
    print(files)


