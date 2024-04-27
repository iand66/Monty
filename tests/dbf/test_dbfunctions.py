import os
from datetime import date
from pytest import mark, param
from src.orm.schema import (
    Album,
    Artist,
    Currency,
    Customer,
    Employee,
    Genre,
    Invoice,
    Invoiceitem,
    Mediatype,
    Playlist,
    Playlisttrack,
    Track,
)

from src.orm.dbfunctions import dbSelect, dbInsert, dbUpdate, dbDelete
from src.helper import engine


# Verify build of test database
@mark.order(1)
def test_dbBuild(dbBuild):
    assert os.path.exists(engine.url.database) is True


@mark.order(2)
@mark.parametrize(
    "classname, tablename",
    [
        param(Album, "albums", id="Album"),
        param(Artist, "artists", id="Artist"),
        param(Currency, "currencies", id="Currency"),
        param(Customer, "customers", id="Customer"),
        param(Employee, "employees", id="Employee"),
        param(Genre, "genres", id="Genres"),
        param(Invoice, "invoices", id="Invoice"),
        param(Invoiceitem, "invoiceitems", id="Invoiceitem"),
        param(Mediatype, "mediatypes", id="Mediatype"),
        param(Playlist, "playlists", id="Playlist"),
        param(Playlisttrack, "playlisttracks", id="Playlisttrack"),
        param(Track, "tracks", id="Track"),
    ],
)
def test_dbSelect(get_db, get_count, classname, tablename):
    num = get_count(tablename)
    print(f"{classname} contains {num} entries")
    assert len(dbSelect(get_db, classname, **{"Id": "%"})) == num


# Verify dbInsert of new records to each test database table
# def dbInsert(session, data: Base) -> bool:
@mark.order(3)
@mark.parametrize(
    "tablename, data",
    [
        param(Artist, {"ArtistName": "Test Artist"}, id="Artist"),
        param(Album, {"AlbumTitle": "Test Album", "ArtistId": "276"}, id="Album"),
        param(
            Currency,
            {
                "Code": "XXX",
                "Number": 999,
                "Decimals": 2,
                "Description": "Test Currency",
            },
            id="Currency",
        ),
        param(
            Customer,
            {
                "Firstname": "Test",
                "Lastname": "User",
                "Email": "test@somewhere.com",
                "SupportRepId": "1",
            },
            id="Customer",
        ),
        param(
            Employee,
            {
                "Lastname": "Employee",
                "Firstname": "Test",
                "Title": "Temporary Employee",
                "ReportsTo": "1",
                "Email": "test@somewhere.com",
            },
            id="Employee",
        ),
        param(Genre, {"GenreName": "Unbearable"}, id="Genres"),
        param(Mediatype, {"MediaTypeName": "Unrecognised Format"}, id="Mediatype"),
        param(Playlist, {"PlaylistName": "Unbearable"}, id="Playlist"),
        param(
            Track,
            {
                "TrackName": "Just Don't Do It!",
                "AlbumId": "348",
                "MediaTypeId": "6",
                "GenreId": "26",
                "UnitPrice": "0.01",
                "CurrencyId": 26,
            },
            id="Track",
        ),
        param(
            Playlisttrack, {"PlaylistId": "15", "TrackId": "3504"}, id="Playlisttrack"
        ),
        param(
            Invoice,
            {
                "CustomerId": "60",
                "InvoiceDate": date.today().strftime("%d/%m/%Y %H:%M"),
                "Total": "0.01",
            },
            id="Invoice",
        ),
        param(
            Invoiceitem,
            {
                "InvoiceId": "413",
                "TrackId": "3504",
                "UnitPrice": "0.01",
                "Quantity": "1",
            },
            id="Invoiceitem",
        ),
    ],
)
def test_dbInsert(get_db, tablename, data):
    assert dbInsert(get_db, tablename(**data)) is True


# Verify dbUpdate to dbInsert records
# def dbUpdate(session, table: Base, filter: dict, update: dict) -> bool:
@mark.order(4)
@mark.parametrize(
    "tablename, f_data, t_data",
    [
        param(
            Artist,
            {"ArtistName": "Test Artist"},
            {"ArtistName": "Another Test Artist"},
            id="Artist",
        ),
        param(
            Album,
            {"AlbumTitle": "Test Album"},
            {"AlbumTitle": "Another Test Album"},
            id="Album",
        ),
        param(Currency, {"Code": "XXX"}, {"Code": "ZZZ"}, id="Currency"),
        param(
            Customer,
            {"Email": "test@somewhere.com"},
            {"Company": "ACME Inc"},
            id="Customer",
        ),
        param(
            Employee, {"Email": "test@somewhere.com"}, {"ReportsTo": "2"}, id="Employee"
        ),
        param(
            Genre, {"GenreName": "Unbearable"}, {"GenreName": "Grotesque"}, id="Genres"
        ),
        param(
            Mediatype,
            {"MediaTypeName": "Unrecognised Format"},
            {"MediaTypeName": "Unusable Format"},
            id="Mediatype",
        ),
        param(
            Playlist,
            {"PlaylistName": "Unbearable"},
            {"PlaylistName": "Grotesque"},
            id="Playlist",
        ),
        param(Track, {"AlbumId": "348"}, {"Composer": "Should B Shot"}, id="Track"),
        param(
            Invoice,
            {"CustomerId": "60"},
            {"InvoiceDate": date.today().strftime("%d/%m/%Y %H:%M")},
            id="Invoice",
        ),
        param(Invoiceitem, {"InvoiceId": "413"}, {"Quantity": "5"}, id="Invoiceitem"),
    ],
)
def test_dbUpdate(get_db, tablename, f_data, t_data):
    assert dbUpdate(get_db, tablename, f_data, t_data) is True


# Verify dbDelete of dbInsert records
# def dbDelete(session, table: Base, **kwargs) -> bool:
@mark.order(5)
@mark.parametrize(
    "tablename, data",
    [
        param(Invoiceitem, {"InvoiceId": "413"}, id="Invoiceitem"),
        param(Invoice, {"CustomerId": "60"}, id="Invoice"),
        param(Playlisttrack, {"PlaylistId": "15"}, id="Playlisttrack"),
        param(Track, {"TrackName": "Just Don't Do It!"}, id="Track"),
        param(Playlist, {"PlaylistName": "Grotesque"}, id="Playlist"),
        param(Mediatype, {"MediaTypeName": "Unusable Format"}, id="Mediatype"),
        param(Genre, {"GenreName": "Grotesque"}, id="Genres"),
        param(Employee, {"Email": "test@somewhere.com"}, id="Employee"),
        param(Customer, {"Email": "test@somewhere.com"}, id="Customer"),
        param(Currency, {"Code": "ZZZ"}, id="Currency"),
        param(Album, {"AlbumTitle": "Another Test Album"}, id="Album"),
        param(Artist, {"ArtistName": "Another Test Artist"}, id="Artist"),
    ],
)
def test_dbDelete(get_db, tablename, data):
    assert dbDelete(get_db, tablename, **(data)) is True
