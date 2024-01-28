import os
from pytest import mark, param
from raw.csvhelper import csvRead, csvDictReader, csvWrite, csvDictWriter
from orm.schema import *
from orm.dbfunctions import dbSelectAll

@mark.parametrize('filename, record',
    [param('./sam/csv/albums.csv', 347, id='Albums'),
     param('./sam/csv/artists.csv', 275, id='Artists'),
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
def test_csvRead(setup, filename, record):
    if os.path.exists(filename):
        assert len(csvRead(filename, True))-1 == record

@mark.parametrize('filename, record',
    [param('./sam/csv/albums.csv', 347, id='Albums'),
     param('./sam/csv/artists.csv', 275, id='Artists'),
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
def test_csvDictReader(setup, filename, record):
    if os.path.exists(filename):
        assert len(csvDictReader(filename, True)) == record

@mark.parametrize('filename, object',
    [param('albums.csv', Album, id='Albums'),
     param('artists.csv', Artist, id='Artists'),
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
def test_csvWrite(setup, temp, filename, object):
    assert csvWrite(temp/filename, dbSelectAll(setup.engine, object, False, False), False) == True

@mark.parametrize('filename, object',
    [param('albums.csv', Album, id='Albums'),
     param('artists.csv', Artist, id='Artists'),
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
def test_csvDictWriter(setup, temp, filename, object):
    assert csvDictWriter(temp/filename, dbSelectAll(setup.engine, object, False, False), False) == True
