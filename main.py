from sqlalchemy import create_engine, table
from lib.apputils import config, logSetup
from orm.schema import Genre
from orm.dbfunctions import dbSelectAll

if __name__ == '__main__':
    appcfg = config('./ini/globals.ini')
    logger = logSetup(appcfg['LOGCFG']['logcfg'], appcfg['LOGCFG']['logloc'], eval(appcfg['LOGCFG']['logecho']))
    engine = create_engine(appcfg['DBTST']['dbType'] + appcfg['DBTST']['dbName'])
    #dbInit(engine)
    #dbFill(engine,'./sam/csv/import.csv',appcfg['DBTST']['dbName'],False)
    #x = dbSelectAll(engine, Genre, True)
    #print(x, type(x))
    y = dbSelectAll(engine, table('Fred'), True)
    print(y, type(y))
    
    
