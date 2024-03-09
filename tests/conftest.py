import os
from pytest import fixture
from src.orm.schema import *
from src.orm.dbutils import dbKill, dbInit, dbFill
from src.helper import appcfg, mode, echo, trace, engine, session

# Setup testing environment
@fixture(scope="session")
def get_db():
    db = session()

    try:
        yield db
    finally:
        db.close()

# Setup clean database    
@fixture(scope="session")
def dbBuild(get_db):
    """
    dbKill - Delete test database if exists
    dbInit - Create new database shell - orm/schema
    dbFill - Populate new database
    """
    session = get_db
    
    if mode:
        if os.path.exists(appcfg['DBCFG']['dbName']): 
            assert dbKill(appcfg['DBCFG']['dbName'], echo) == True
            assert dbInit(engine, echo) == True
        else:
            assert dbInit(engine, echo) == True
            
        assert dbFill(session, './sam/csv/import.csv', appcfg['DBCFG']['dbName'], echo, trace) == True
    else:
        if os.path.exists(appcfg['DBTST']['dbName']): 
            assert dbKill(appcfg['DBTST']['dbName'], echo) == True
            assert dbInit(engine, echo) == True
        else:
            assert dbInit(engine, echo) == True
            
        assert dbFill(session, './sam/csv/import.csv', appcfg['DBTST']['dbName'], echo, trace) == True
    
    #yield session
    
# Define tmp directory
# TODO tmp directory?
@fixture(scope="session")
def temp(tmp_path_factory):
    """
    Create tempdir for CSV I/O tests
    """
    tempdir = tmp_path_factory.mktemp('tmp')
    return tempdir