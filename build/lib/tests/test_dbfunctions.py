import pytest, os
from sqlalchemy import create_engine
from lib.apputils import config, logSetup
from orm.schema import *
from orm.dbutils import dbKill, dbInit, dbFill
from orm.dbfunctions import dbSelectAll

# TODO Demo Capsys Monkeypatch Raises(Error)
# TODO Move common to conftest

appcfg = config('./ini/globals.ini')
logger = logSetup(appcfg['LOGCFG']['logcfg'], appcfg['LOGCFG']['logloc'], eval(appcfg['LOGCFG']['logecho']))
engine = create_engine(appcfg['DBTST']['dbType'] + appcfg['DBTST']['dbName'], connect_args={"check_same_thread":False})

@pytest.fixture(scope='session')
def setup(request):
    if os.path.exists(appcfg['DBTST']['dbName']): 
        print(os.path.exists(appcfg['DBTST']['dbName']))
        assert dbKill(appcfg['DBTST']['dbName']) == True
        assert dbInit(engine) == True
    else:
        assert dbInit(engine) == True
        
    assert dbFill(engine, './sam/csv/import.csv', appcfg['DBTST']['dbName'], False) == True

# TODO Reusable param list?
@pytest.mark.parametrize(
        'tablename, record',
        [pytest.param(Artist, 275, id='Artists'),
         pytest.param(Genre, 25, id='Genres'),
         pytest.param(Mediatype, 5, id='Mediatype'),
         pytest.param(Playlist, 14, id='Playlist'),
         pytest.param(Album, 347, id='Album'),
         pytest.param(Employee, 8, id='Employee'),
         pytest.param(Customer, 59, id='Customer'),
         pytest.param(Invoice, 412, id='Invoice'),
         pytest.param(Track, 3503, id='Track'),
         pytest.param(Invoiceitem, 2240, id='Invoiceitem'),
         pytest.param(Playlisttrack, 8715, id='Playlisttrack')] 
        )
def test_SelectAll(setup, tablename, record):
    print(f'SelectAll {tablename.__tablename__}, {record}')
    assert len(dbSelectAll(engine, tablename, False)) == record

#def test_UpdateAll(setup, tablename):
#def test_DeleteAll(setup, tablename)