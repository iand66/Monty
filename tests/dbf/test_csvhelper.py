import os
from pytest import mark, param
from src.raw.csvhelper import csvRead, csvDictReader, csvWrite, csvDictWriter
from src.orm.schema import *
from src.orm.dbfunctions import dbSelect
from src.helper import trace

# Verify sample files loaded to test database
# def csvRead(filename:str) -> list:
@mark.parametrize('filename, record',
    [param('./sam/csv/albums.csv', 347, id='Albums'),
     param('./sam/csv/artists.csv', 275, id='Artists'),
     param('./sam/csv/currency.csv', 152, id='Currency'),
     param('./sam/csv/customers.csv', 59, id='Customers'),
     param('./sam/csv/employees.csv', 8, id='Employees'),
     param('./sam/csv/genres.csv', 25, id='Genres'),
     param('./sam/csv/invoices.csv', 412, id='Invoices'),
     param('./sam/csv/invoiceitems.csv', 2240, id='Invoiceitems'),
     param('./sam/csv/mediatypes.csv', 5, id='Mediatypes'),
     param('./sam/csv/playlists.csv', 14, id='Playlists'),
     param('./sam/csv/playlisttracks.csv', 8715, id='Playlisttracks'),
     param('./sam/csv/tracks.csv', 3503, id='Tracks')]
     )
def test_csvRead(get_db, filename, record):
    if os.path.exists(filename):
        assert len(csvRead(filename))-1 == record

# Verify sample files loaded to test database
# def csvDictReader(filename:str) -> list:
@mark.parametrize('filename, record',
    [param('./sam/csv/albums.csv', 347, id='Albums'),
     param('./sam/csv/artists.csv', 275, id='Artists'),
     param('./sam/csv/currency.csv', 152, id='Currency'),
     param('./sam/csv/customers.csv', 59, id='Customers'),
     param('./sam/csv/employees.csv', 8, id='Employees'),
     param('./sam/csv/genres.csv', 25, id='Genres'),
     param('./sam/csv/invoices.csv', 412, id='Invoices'),
     param('./sam/csv/invoiceitems.csv', 2240, id='Invoiceitems'),
     param('./sam/csv/mediatypes.csv', 5, id='Mediatypes'),
     param('./sam/csv/playlists.csv', 14, id='Playlists'),
     param('./sam/csv/playlisttracks.csv', 8715, id='Playlisttracks'),
     param('./sam/csv/tracks.csv', 3503, id='Tracks')]
     )
def test_csvDictRead(get_db, filename, record):
    if os.path.exists(filename):
        assert len(csvDictReader(filename)) == record

# Verify CSV write from test database
# def csvWrite(filename:str, data:list) -> bool: 
@mark.parametrize('filename, table',
    [param('albums.csv', Album, id='Albums'),
     param('artists.csv', Artist, id='Artists'),
     param('customers.csv', Customer, id='Customers'),
     param('currency.csv', Currency, id='Currency'),
     param('employees.csv', Employee, id='Employees'),
     param('genres.csv', Genre, id='Genres'),
     param('invoices.csv', Invoice, id='Invoices'),
     param('invoiceitems.csv', Invoiceitem, id='Invoiceitems'),
     param('mediatypes.csv', Mediatype, id='Mediatypes'),
     param('playlists.csv', Playlist, id='Playlists'),
     param('playlisttracks.csv', Playlisttrack, id='Playlisttracks'),
     param('tracks.csv', Track, id='Tracks')]
     )
def test_csvWrite(get_db, temp, filename, table):
    assert csvWrite(temp+'\\'+filename, dbSelect(get_db, table, trace, **{'Id':'%'})) == True

# Verify CSV write from test database
# def csvDictWriter(filename:str, data:dict) -> bool:
@mark.parametrize('filename, table',
    [param('albums.csv', Album, id='Albums'),
     param('artists.csv', Artist, id='Artists'),
     param('currency.csv', Currency, id='Currency'),
     param('customers.csv', Customer, id='Customers'),
     param('employees.csv', Employee, id='Employees'),
     param('genres.csv', Genre, id='Genres'),
     param('invoices.csv', Invoice, id='Invoices'),
     param('invoiceitems.csv', Invoiceitem, id='Invoiceitems'),
     param('mediatypes.csv', Mediatype, id='Mediatypes'),
     param('playlists.csv', Playlist, id='Playlists'),
     param('playlisttracks.csv', Playlisttrack, id='Playlisttracks'),
     param('tracks.csv', Track, id='Tracks')]
     )
def test_csvDictWrite(get_db, temp, filename, table):
    assert csvDictWriter(temp/filename, dbSelect(get_db, table, trace, **{'Id':'%'})) == True
