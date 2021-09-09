#importamos librerias 
import pandas_datareader.data as web
from statistics import stdev as de

#función para descargar precios ajustados 
def get_adj_closes(tickers, start_date=None, end_date=None):
    closes = web.DataReader(name=tickers, data_source='yahoo', start=start_date, end=end_date)
    closes = closes['Adj Close']
    closes.sort_index(inplace=True)
    return closes

def sharpe(lista, rf):
    sharpe_ = (sum(lista) / len(lista) - (rf / 12)) / de(lista)
    return sharpe_