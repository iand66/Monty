from fastapi.testclient import TestClient
from pytest import mark, param
from main import app

client = TestClient(app)

def test_home():
    response = client.get('/')
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
    assert response.status_code == 200
    assert len(response.json()) == record
