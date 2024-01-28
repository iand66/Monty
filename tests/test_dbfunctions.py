from pytest import mark, param
from orm.schema import *
from orm.dbfunctions import dbSelectAll

@mark.parametrize('tablename, record',
    [param(Album, 347, id='Album'),
     param(Artist, 275, id='Artists'),
     param(Customer, 59, id='Customer'),
     param(Employee, 8, id='Employee'),   
     param(Genre, 25, id='Genres'),
     param(Invoice, 412, id='Invoice'),
     param(Invoiceitem, 2240, id='Invoiceitem'),
     param(Mediatype, 5, id='Mediatype'),
     param(Playlist, 14, id='Playlist'),
     param(Playlisttrack, 8715, id='Playlisttrack'),
     param(Track, 3503, id='Track')]
     )
def test_SelectAll(setup, tablename, record):
    assert len(dbSelectAll(setup.engine, tablename, False, False)) == record

# TODO def test_UpdateAll(setup, ...):
# TODO def test_DeleteAll(setup, ...)