from pytest import mark, param

from src.orm.schema import *
from src.orm.dbfunctions import dbSelect, dbInsert

# def dbUpdate(session, table:Base, filter:dict, update:dict, echo:bool, trace:bool,) -> int:
# def dbDelete(session, table:Base, echo:bool, trace:bool, **kwargs) -> int:

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
def test_dbSelect(setup, tablename, record):
    assert len(dbSelect(setup, tablename, False, False, **{'Id':'%'})) == record

# TODO Rework this!
@mark.parametrize('tablename, record, data',
    [param(Artist, 275, {'ArtistName':'Test Artist'}, id='Artists'),
     param(Album, 347, {'AlbumTitle':'Test Album','ArtistId':'276'}, id='Album'),
     param(Customer, 59, {'Firstname':'Test','Lastname':'User','Email':'test@somewhere.com','SupportRepId':'1'}, id='Customer'),
     param(Employee, 8, {'Lastname':'Employee','Firstname':'Test','Title':'Temporary Employee','ReportsTo':'1','Email':'test@somewhere.com'}, id='Employee'),
     param(Genre, 25, {'GenreName':'Unbearable'}, id='Genres'),
     param(Mediatype, 5, {'MediaTypeName':'Unrecognised Format'}, id='Mediatype'),
     param(Playlist, 14, {'PlaylistName':'Unbearable'}, id='Playlist'),
     param(Track, 3503, {'TrackName':'Just Don\'t Do It!','AlbumId':'348','MediaTypeId':'6','GenreId':'26','UnitPrice':'0.01'}, id='Track'),
     param(Playlisttrack, 8715, {'PlaylistId':'15','TrackId':'3504'}, id='Playlisttrack'),
     param(Invoice, 412, {'CustomerId':'60','InvoiceDate':datetime.now().strftime("%d/%m/%Y %H:%M"),'Total':'0.01'}, id='Invoice'),
     param(Invoiceitem, 2240, {'InvoiceId':'413','TrackId':'3504','UnitPrice':'0.01','Quantity':'1'}, id='Invoiceitem'),]   
     )
def test_dbInsert(setup, tablename, record, data):
    assert dbInsert(setup, tablename(**data), False, False) == record+1