import os
from pytest import fixture
from src.orm.schema import *
from src.orm.dbutils import dbKill, dbInit, dbFill
from src.helper import appcfg, mode, trace, engine, session

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
    if mode:
        dbname = appcfg.get('DBCFG','dblive')
    else:
        dbname = appcfg.get('DBCFG','dbtest')
    
    if os.path.exists(dbname): 
        assert dbKill(dbname) == True
        assert dbInit(engine) == True
    else:
        assert dbInit(engine) == True
            
    assert dbFill(get_db, './sam/csv/import.csv', dbname, trace) == True
    
# Define tmp directory
# TODO tmp directory?
@fixture(scope="session")
def temp(tmp_path_factory):
    """
    Create tempdir for CSV I/O tests
    """
    tempdir = tmp_path_factory.mktemp('tmp')
    return tempdir