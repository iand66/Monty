from pytest import mark, param
from orm.schema import *
from orm.dbfunctions import dbSelectAll

@mark.parametrize(
        'tablename, record',
        [param(Artist, 275, id='Artists'),
         param(Genre, 25, id='Genres'),
         param(Mediatype, 5, id='Mediatype'),
         param(Playlist, 14, id='Playlist'),
         param(Album, 347, id='Album'),
         param(Employee, 8, id='Employee'),
         param(Customer, 59, id='Customer'),
         param(Invoice, 412, id='Invoice'),
         param(Track, 3503, id='Track'),
         param(Invoiceitem, 2240, id='Invoiceitem'),
         param(Playlisttrack, 8715, id='Playlisttrack')] 
        )
def test_SelectAll(setup, tablename, record):
    print(f'SelectAll {tablename.__tablename__}, {record}')
    assert len(dbSelectAll(setup.engine, tablename, False)) == record

# TODO def test_UpdateAll(setup, ...):
# TODO def test_DeleteAll(setup, ...)