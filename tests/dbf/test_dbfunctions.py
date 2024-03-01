import os

from datetime import date
from pytest import mark, param

from src.orm.schema import *
from src.orm.dbfunctions import dbSelect, dbInsert, dbUpdate, dbDelete

# Verify build of test database
@mark.order(1)
def test_dbBuild(build, get_db):
    assert os.path.exists(get_db[1]['DBTST']['dbName'])

# Verify dbSelect matches known record count
# def dbSelect(session, table:Base, echo:bool, trace:bool, filter:dict) -> list:
@mark.order(2)
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
def test_dbSelect(get_db, tablename, record):
    assert len(dbSelect(get_db[0], tablename, get_db[3], get_db[4], **{'Id':'%'})) == record

# Verify dbInsert of new records to each test database table        
# def dbInsert(session, table:Base, echo:bool, trace:bool) -> int:
@mark.order(3)
@mark.parametrize('tablename, data',
    [param(Artist, {'ArtistName':'Test Artist'}, id='Artists'),
    param(Album, {'AlbumTitle':'Test Album','ArtistId':'276'}, id='Album'),
    param(Customer, {'Firstname':'Test','Lastname':'User','Email':'test@somewhere.com','SupportRepId':'1'}, id='Customer'),
    param(Employee, {'Lastname':'Employee','Firstname':'Test','Title':'Temporary Employee','ReportsTo':'1','Email':'test@somewhere.com'}, id='Employee'),
    param(Genre, {'GenreName':'Unbearable'}, id='Genres'),
    param(Mediatype, {'MediaTypeName':'Unrecognised Format'}, id='Mediatype'),
    param(Playlist, {'PlaylistName':'Unbearable'}, id='Playlist'),
    param(Track, {'TrackName':'Just Don\'t Do It!','AlbumId':'348','MediaTypeId':'6','GenreId':'26','UnitPrice':'0.01'}, id='Track'),
    param(Playlisttrack, {'PlaylistId':'15','TrackId':'3504'}, id='Playlisttrack'),
    param(Invoice, {'CustomerId':'60','InvoiceDate':date.now().strftime("%d/%m/%Y %H:%M"),'Total':'0.01'}, id='Invoice'),
    param(Invoiceitem, {'InvoiceId':'413','TrackId':'3504','UnitPrice':'0.01','Quantity':'1'}, id='Invoiceitem')]   
    )
def test_dbInsert(get_db, tablename, data):
    assert dbInsert(get_db[0], tablename(**data), get_db[3], get_db[4]) == True

# Verify dbUpdate to dbInsert records
# def dbUpdate(session, table:Base, from:dict, to:dict, echo:bool, trace:bool,) -> int:
@mark.order(4)
@mark.parametrize('tablename, f_data, t_data',
    [param(Artist, {'ArtistName':'Test Artist'}, {'ArtistName':'Another Test Artist'}, id='Artists'),
    param(Album, {'AlbumTitle':'Test Album'}, {'AlbumTitle':'Another Test Album'}, id='Album'),
    param(Customer, {'Email':'test@somewhere.com'},{'Company':'ACME Inc'}, id='Customer'),
    param(Employee, {'Email':'test@somewhere.com'}, {'ReportsTo':'2'}, id='Employee'),
    param(Genre, {'GenreName':'Unbearable'}, {'GenreName':'Grotesque'}, id='Genres'),
    param(Mediatype, {'MediaTypeName':'Unrecognised Format'}, {'MediaTypeName':'Unusable Format'}, id='Mediatype'),
    param(Playlist, {'PlaylistName':'Unbearable'}, {'PlaylistName':'Grotesque'}, id='Playlist'),
    param(Track, {'AlbumId':'348'}, {'Composer':'Should B Shot'}, id='Track'),
    param(Invoice, {'CustomerId':'60'}, {'InvoiceDate':date.now().strftime("%d/%m/%Y %H:%M")}, id='Invoice'),
    param(Invoiceitem, {'InvoiceId':'413'},{'Quantity':'5'}, id='Invoiceitem')]   
    )
def test_dbUpdate(get_db, tablename, f_data, t_data):
    assert dbUpdate(get_db[0], tablename, f_data, t_data, get_db[3], get_db[4]) == True

# Verify dbDelete of dbInsert records
# def dbDelete(session, table:Base, echo:bool, trace:bool, filter:dict) -> int:
@mark.order(5)
@mark.parametrize('tablename, data',
    [param(Invoiceitem, {'InvoiceId':'413'}, id='Invoiceitem'),
    param(Invoice, {'CustomerId':'60'}, id='Invoice'),
    param(Playlisttrack, {'PlaylistId':'15'}, id='Playlisttrack'),
    param(Track, {'TrackName':'Just Don\'t Do It!'}, id='Track'),
    param(Playlist, {'PlaylistName':'Grotesque'}, id='Playlist'),
    param(Mediatype, {'MediaTypeName':'Unusable Format'}, id='Mediatype'),
    param(Genre, {'GenreName':'Grotesque'}, id='Genres'),
    param(Employee, {'Email':'test@somewhere.com'}, id='Employee'),
    param(Customer, {'Email':'test@somewhere.com'}, id='Customer'),
    param(Album, {'AlbumTitle':'Another Test Album'}, id='Album'),
    param(Artist, {'ArtistName':'Another Test Artist'}, id='Artists')]   
    )
def test_dbDelete(get_db, tablename, data):
    assert dbDelete(get_db[0], tablename, get_db[3], get_db[4], **(data)) == True