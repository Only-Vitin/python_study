from sqlalchemy import create_engine

from _constantes import *


def mysql_connection(host, user, passwd, database=None):
    engine = create_engine(f'mysql+pymysql://{user}:{passwd}@{host}/{database}')
    return engine.connect()

connection = mysql_connection(host, user, passw, db)