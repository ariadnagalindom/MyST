from data import precios_mensuales, precios_ipc
from main import v_port_ini, v_port_pas, capital

import pandas as pd

df=pd.DataFrame({'TimeStamp': precios_mensuales.index, 'Capital': v_port_pas})
rends=[(v_port_pas[i+1] / v_port_pas[i])-1 for i in range(0, len(v_port_pas)-1)]
rends.insert(0,0)
rends_cum= [(v_port_pas[i]/ v_port_ini)-1 for i in range(0, len(v_port_pas))]

losses= [df['Capital'][i]-capital for i in range(0, len(v_port_pas))]

df['Rends']= rends
df['Rends_acums']= rends_cum
df['ganancias/perdidas']= losses

y=[precios_ipc['^MXX'][i]/ sum(precios_ipc['^MXX']) for i in range(0, len(precios_ipc))]
y2= [df['Capital'][i]/ sum(df['Capital'])for i in range(0, len(df['Capital']))]

