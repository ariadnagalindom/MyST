#primero corrimos:   pip install MetaTrader5 
import MetaTrader5 as mt

meta_path='C:\Program Files\MetaTrader 5 Terminal\\terminal64.exe'
login_account=5400337
password= 'yKptOu7U'
server_name='FxPro-MT5'

connection=mt.initialize(path=meta_path, login=login_account,password=password,server=server_name)
#print(mt.last_error())
#mt.account_info()