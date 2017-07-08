'''mysqlclient 作为mysqldb 的后继者，可以与最新版本的Python配合，
也可以与sqlalchemy 合作'''
from sqlalchemy import engine,create_engine, Table, Column, Integer,Float, String,MetaData, ForeignKey, DateTime
from datetime import date, datetime
import datetime
aengine = create_engine('mysql://root:223223@localhost/talk_is_cheap')
metadata = MetaData()
rbtickdata = Table('rbtickdata', metadata,
                   Column('TDATETIME', DateTime, primary_key=True),
                   Column('CONTRACTID', String(50), primary_key=True),
                   Column('LASTPX', Float),
                   Column('HIGHPX', Float),
                   Column('LOWPX', Float),
                   Column('CurrentQ', Integer),
                   Column('TotalQ', Integer),
                   Column('INITOPENINTS', Integer),
                   Column('OPENINTS', Integer),
                   Column('INTSCHG', Integer),
                   Column('RISELIMIT', Float),
                   Column('FALLLIMIT', Float),
                   Column('PRESETTLE', Float),
                   Column('PRECLOSE', Float),
                   Column('SELLPX01', Float),
                   Column('BUYPX01', Float),
                   Column('SELLVOL01', Integer),
                   Column('BUYVOL01', Integer),
                   Column('AVGPX', Float),
                   Column('LOCALTIME', DateTime))
metadata.create_all(aengine)
# aengine.connect()
