from sqlalchemy import create_engine
from lib.apputils import config
from orm.dbutils import dbInit, dbFill, dbKill
from orm.dbfunctions import dbInsert, dbSelect, dbUpdate, dbDelete
from orm.dbfunctions import dbSelectAll, dbUpdateAll, dbDeleteAll
from orm.schema import Genre, Employee, Playlisttrack

appcfg = config('./ini/globals.ini')
engine = create_engine(appcfg['DBTST']['dbType'] + appcfg['DBTST']['dbName'])
    
def setup_module():
    # Prep test environment
    dbInit(engine)
    dbFill(engine,'./sam/csv/import.csv',appcfg['DBTST']['dbName'],False)

def test_dbInsert_pass():
    x = dbInsert(engine, Genre(GenreName='Screaming'), True) # Success does not exist
    assert x > 0

def test_dbInsert_fail():
    x = dbInsert(engine, Genre(GenreName='Screaming'), True) # Fail unique constraint
    assert x == None

def test_dbSelect_pass():
    x = dbSelect(engine, Genre, {'GenreName':'Screaming'}, True) # Success record exists
    assert x != None

def test_dbSelect_fail():
    x = dbSelect(engine, Genre, {'GenreName':'Blue Murder'}, True) # Fail record does not exist
    assert x == None

def test_dbUpdate_pass():
    x = dbUpdate(engine, Genre, {'GenreName':'Screaming'}, 'GenreName', 'Blue Murder', True) # Success renamed
    assert x > 0

def test_dbUpdate_fail():
    x = dbUpdate(engine, Genre, {'GenreName':'Hypnosis'}, 'GenreName', 'Blue Murder', True) # Fail record does not exist
    assert x == 0
    
def test_dbDelete_pass():
    x = dbDelete(engine, Genre, {'GenreName':'Blue Murder'}, True) # Success record exists
    assert x > 0

def test_dbDelete_fail():
    x = dbDelete(engine, Genre, {'GenreName':'Screaming'}, True) # Fail record does not exist
    assert x == 0
    
def test_dbSelectAll_pass():
    x = dbSelectAll(engine, Genre, True) # Success table exists
    assert x != None

def test_dbSelectAll_fail():
    #TODO Missing tablename
    pass

def test_dbUpdateAll_pass():
    x = dbUpdateAll(engine, Employee, 'Title', 'New Title', True) # Success table exists
    assert x > 0

def test_dbUpdateAll_fail():
    #TODO Missing tablename
    #TODO Missing attribute
    pass

def test_dbDelete_pass():
    x = dbDeleteAll(engine, Playlisttrack, True) # Success table exists
    assert x > 0

def test_dbDelete_fail():
    #TODO Missing tablename
    pass

def teardown_module():
    # Cleanup test database
    dbKill(appcfg['DBTST']['dbName'])