import os

from pytest import fixture
from icecream import ic
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.lib.apputils import config, logSetup
from src.orm.schema import *
from src.orm.dbutils import dbKill, dbInit, dbFill

@fixture(scope="session")
def setup(request):
    appcfg = config('./ini/globals.ini')
    echo = eval(appcfg['LOGCFG']['logecho'])
    trace = eval(appcfg['LOGCFG']['trace'])
    logger = logSetup(appcfg['LOGCFG']['logcfg'], appcfg['LOGCFG']['logloc'], echo, trace)
    #engine = create_engine(appcfg['DBCFG']['dbType'] + appcfg['DBCFG']['dbName'], connect_args={"check_same_thread":False})
    engine = create_engine(appcfg['DBTST']['dbType'] + appcfg['DBTST']['dbName'], connect_args={"check_same_thread":False})
    Session = sessionmaker(bind=engine)
    session = Session()
    
    if os.path.exists(appcfg['DBTST']['dbName']): 
        assert dbKill(appcfg['DBTST']['dbName'], echo) == True
        assert dbInit(engine, echo) == True
    else:
        assert dbInit(engine, echo) == True
        
    assert dbFill(session, './sam/csv/import.csv', appcfg['DBTST']['dbName'], echo, trace) == True
    
    yield session

# TODO tmp =./sam/tmp
@fixture(scope="session")
def temp(tmp_path_factory):
    tempdir = tmp_path_factory.mktemp('tmp')
    return tempdir