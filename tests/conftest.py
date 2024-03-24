import os

from pytest import fixture
from sqlalchemy import text

from src.helper import appcfg, engine, mode, session, trace
from src.orm.dbutils import dbFill, dbInit, dbKill
from src.orm.schema import *

# Get testing database name
@fixture(scope="session")
def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()

# Setup testing environment
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
            
    if get_db.bind.name == 'sqlite':
        get_db.execute(text('pragma foreign_keys=on'))
    
    assert dbFill(get_db, './sam/csv/import.csv', dbname, trace) == True
    
# Define tmp directory
# TODO tmp directory?
@fixture(scope="session")
def temp():
    """
    Create tempdir for CSV I/O tests
    """
    if not os.path.exists('./sam/tmp'):
        os.makedirs('./sam/tmp')
    tmpdir = './sam/tmp'
    return tmpdir