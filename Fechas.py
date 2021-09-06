from numpy.lib.function_base import append
from numpy.testing._private.utils import print_assert_equal
import pandas as pd
import numpy as np
from pandas.core.frame import DataFrame
import yfinance as yf
from datetime import date, datetime
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
    fechas.append(files[-12:-8] + files[-8:-6] + files[-6:-4])



fcd = pd.DataFrame()

fcd['Date'] = fechas 

dates = list(fcd['Date'])
print(dates)

print(dates[0])

g = []
i = 0

for i in range(len(dates)):
    fechas = pd.to_datetime(dates[i], format='%Y/%m/%d')
    g.append(fechas)

print(g)


l = pd.DataFrame()
l['Date'] = g
v = l.sort_values(['Date'])
print(v)





