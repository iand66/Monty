import os
from pytest import fixture
from sqlalchemy import create_engine
from lib.apputils import config, logSetup
from orm.schema import *
from orm.dbutils import dbKill, dbInit, dbFill

@fixture(scope='session')
def setup(request):
    appcfg = config('./ini/globals.ini')
    logger = logSetup(appcfg['LOGCFG']['logcfg'], appcfg['LOGCFG']['logloc'], eval(appcfg['LOGCFG']['logecho']))
    #engine = create_engine(appcfg['DBCFG']['dbType'] + appcfg['DBCFG']['dbName'], connect_args={"check_same_thread":False})
    engine = create_engine(appcfg['DBTST']['dbType'] + appcfg['DBTST']['dbName'], connect_args={"check_same_thread":False})
    

    if os.path.exists(appcfg['DBTST']['dbName']): 
        assert dbKill(appcfg['DBTST']['dbName'], eval(appcfg['LOGCFG']['logecho'])) == True
        assert dbInit(engine, eval(appcfg['LOGCFG']['logecho'])) == True
    else:
        assert dbInit(engine, eval(appcfg['LOGCFG']['logecho'])) == True
        
    assert dbFill(engine, './sam/csv/import.csv', appcfg['DBTST']['dbName'], eval(appcfg['LOGCFG']['logecho'])) == True

    yield engine