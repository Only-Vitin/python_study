from sqlalchemy import create_engine, Engine

from _constantes import HOST, USER, PASSWD, DB


def mysql_connection(host, user, passwd, database=None) -> Engine:
    engine = create_engine(f"mysql+pymysql://{user}:{passwd}@{host}/{database}")
    return engine.connect()


connection = mysql_connection(HOST, USER, PASSWD, DB)
