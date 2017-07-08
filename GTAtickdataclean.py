# from pyodbc import *
import time

# from sqlalchemy import engine,create_engine
# aengine = create_engine("mssql+pyodbc://sa:223223@127.0.0.1:1433/GTA_MFL1_TAQ_201206_new?driver=SQL+Server+Native+Client+11.0")
# print(aengine.connect())
import sqlalchemy
print( sqlalchemy.__version__)

# import pyodbc
# cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=127.0.0.1;DATABASE=GTA_MFL1_TAQ_201206_new;UID=sa;PWD=223223')
# cursor = cnxn.cursor()
# print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
# cursor.execute("SELECT * FROM MFL1_TAQ_AU1212_201206")
# tables = cursor.fetchall()
# print(tables)
# print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))