from sqlalchemy import create_engine
from lib.apputils import config, logSetup
from orm.schema import Genre
from orm.dbutils import dbInit, dbFill
from orm.dbfunctions import dbSelectAll

if __name__ == '__main__':
    appcfg = config('./ini/globals.ini')
    logger = logSetup(appcfg['LOGCFG']['logcfg'], appcfg['LOGCFG']['logloc'], eval(appcfg['LOGCFG']['logecho']))
    engine = create_engine(appcfg['DBTST']['dbType'] + appcfg['DBTST']['dbName'])
    #dbInit(engine)
    #dbFill(engine,'./sam/csv/import.csv',appcfg['DBTST']['dbName'],False)
    #x = dbSelectAll(engine, Genre, eval(appcfg['LOGCFG']['trace']))
    #print(type(x), x)