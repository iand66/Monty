from random import randint

from fastapi.testclient import TestClient
from pytest import mark, param

from src.main import app

client = TestClient(app)

def test_home():
    response = client.get('/')
    print(f'Endpoint = /')
    assert response.status_code == 200
    assert response.json() == 'Welcome to Monty'

@mark.parametrize('tablename, record',
    [param('albums', 347, id='Albums'),
     param('artists', 275, id='Artists'),
     param('customers', 59, id='Customers'),
     param('employees', 8, id='Employees'),
     param('genres', 25, id='Genres'),
     param('invoices', 412, id='Invoices'),
     param('mediatypes', 5, id='Mediatypes'),
     param('playlists', 14, id='Playlists'),
     param('tracks', 3503, id='Tracks')]
     )
def test_getall(tablename, record):
    response = client.get(f'/{tablename}')
    print(f'Endpoint = /{tablename} record count {record}')
    assert response.status_code == 200
    assert len(response.json()) == record

@mark.parametrize('tablename, record',
    [param('albums', 347, id='Albums'),
     param('artists', 275, id='Artists'),
     param('customers', 59, id='Customers'),
     param('employees', 8, id='Employees'),
     param('genres', 25, id='Genres'),
     param('invoices', 412, id='Invoices'),
     param('mediatypes', 5, id='Mediatypes'),
     param('playlists', 14, id='Playlists'),
     param('tracks', 3503, id='Tracks')]
     )
def test_getid_pass(tablename, record):
    x = randint(1,record)
    response = client.get(f'/{tablename}/{x}')
    print(f'Endpoint = /{tablename}/{x}')
    assert response.status_code == 200

@mark.parametrize('tablename, record',
    [param('albums', 999, id='Albums'),
     param('artists', 999, id='Artists'),
     param('customers', 99, id='Customers'),
     param('employees', 99, id='Employees'),
     param('genres', 99, id='Genres'),
     param('invoices', 999, id='Invoices'),
     param('mediatypes', 99, id='Mediatypes'),
     param('playlists', 99, id='Playlists'),
     param('tracks', 9999, id='Tracks')]
     )
def test_getid_fail(tablename, record):
    response = client.get(f'/{tablename}/{record}')
    print(f'Endpoint = /{tablename}/{record+1}')
    assert response.status_code == 404

@mark.parametrize('tablename, record',
    [param('albums', '%', id='Albums'),
     param('artists', '%', id='Artists'),
     param('customers', '%', id='Customers'),
     param('employees', '%', id='Employees'),
     param('genres', '%', id='Genres'),
     param('invoices', '%', id='Invoices'),
     param('mediatypes', '%', id='Mediatypes'),
     param('playlists', '%', id='Playlists'),
     param('tracks', '%', id='Tracks')]
     )
def test_getname_pass(tablename, record):
    response = client.get(f'/{tablename}/{record}')
    print(f'Endpoint = /{tablename}/{record}')
    assert response.status_code == 200

@mark.parametrize('tablename, record',
    [param('albums', 'Not Found', id='Albums'),
     param('artists', 'Not Found', id='Artists'),
     param('customers', 'Not Found', id='Customers'),
     param('employees', 'Not Found', id='Employees'),
     param('genres', 'Not Found', id='Genres'),
     param('invoices', 'Not Found', id='Invoices'),
     param('mediatypes', 'Not Found', id='Mediatypes'),
     param('playlists', 'Not Found', id='Playlists'),
     param('tracks', 'Not Found', id='Tracks')]
     )
def test_getname_fail(tablename, record):
    response = client.get(f'/{tablename}/{record}')
    print(f'Endpoint = /{tablename}/{record}')
    assert response.status_code == 404