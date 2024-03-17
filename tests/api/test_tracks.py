from random import randint

from fastapi.testclient import TestClient
from pytest import mark, param

from src.main import app

client = TestClient(app)

# GET All Tracks - PASS
@mark.order(1)
@mark.parametrize("tablename, version, record", 
    [param("tracks", "v1", 3503, id="Tracks")])
def test_getall(tablename: str, version: str, record: int):
    response = client.get(f"/{tablename}/{version}")
    print(f"Endpoint = /{tablename}/{version} records {record}")
    assert response.status_code == 200
    assert len(response.json()) == record

# GET RANDOM Track by Track Id - PASS
@mark.order(2)
@mark.parametrize("tablename, version, record", 
    [param("tracks", "v1", 3503, id="Tracks")])
def test_getid_pass(tablename: str, version: str, record: int):
    x = randint(1, record)
    response = client.get(f"/{tablename}/{version}/id/{x}")
    print(f"Endpoint = /{tablename}/{version}/id/{x}")
    assert response.status_code == 200
    assert len(response.json()) == 1

# GET Tracks by Id - FAIL
@mark.order(3)
@mark.parametrize("tablename, version, record", 
    [param("tracks", "v1", 9999, id="Tracks")])
def test_getid_fail(tablename: str, version: str, record: int):
    response = client.get(f"/{tablename}/{version}/id/{record}")
    print(f"Endpoint = /{tablename}/{version}/id/{record}")
    assert response.status_code == 404
    
# GET Tracks by Name - PASS
@mark.order(7)
@mark.parametrize("tablename, version, name", 
    [param("tracks", "v1", "Test Track%", id="Tracks")])
def test_getname_pass(tablename: str, version: str, name: str):
    response = client.get(f"/{tablename}/{version}/name/{name}")
    print(f"Endpoint = /{tablename}/{version}/name/{name}")
    assert response.status_code == 200

# GET Tracks by Name - FAIL
@mark.order(4)
@mark.parametrize("tablename, version, name", 
    [param("tracks", "v1", "Not Found", id="Tracks")])
def test_getname_fail(tablename: str, version: str, name: str):
    response = client.get(f"/{tablename}/{version}/name/{name}")
    print(f"Endpoint = /{tablename}/{version}/name/{name}")
    assert response.status_code == 404
   
# POST Track by Name - PASS
@mark.order(5)
@mark.parametrize("tablename, version, name", 
    [param("tracks", "v1", "name", id="Tracks")])
def test_postname_pass1(tablename: str, version: str, name: str):
    data = {"TrackName": "Test Track 1",
            "AlbumId": 1,
            "MediaTypeId": 1,
            "GenreId": 12,
            "Composer": "Some Random Dude",
            "Milliseconds": 123456,
            "Bytes": 9876543,
            "UnitPrice": 0.99
            }
    response = client.post(f"/{tablename}/{version}/name/{name}", json=data)
    print(f"Endpoint = /{tablename}/{version}/name/{name}")
    assert response.status_code == 201

# POST Track by Name - PASS
@mark.order(6)
@mark.parametrize("tablename, version, name", 
    [param("tracks", "v1", "name", id="Tracks")])
def test_postname_pass2(tablename: str, version: str, name: str):
    data = {"TrackName": "Test Track 2",
        "AlbumId": 1,
        "MediaTypeId": 1,
        "GenreId": 12,
        "Composer": "Some Random Dude",
        "Milliseconds": 123456,
        "Bytes": 9876543,
        "UnitPrice": 1.99
        }
    response = client.post(f"/{tablename}/{version}/name/{name}", json=data)
    print(f"Endpoint = /{tablename}/{version}/name/{name}")
    assert response.status_code == 201

# POST Track by Name - FAIL
@mark.order(8)
@mark.parametrize("tablename, version, name", 
    [param("tracks", "v1", "name", id="Tracks")])
def test_postname_fail(tablename: str, version: str, name: str):
    data = {"TrackName": "Test Track 1",
            "AlbumId": 1,
            "MediaTypeId": 1,
            "GenreId": 12,
            "Composer": "Some Random Dude",
            "Milliseconds": 123456,
            "Bytes": 9876543,
            "UnitPrice": 0.99
            }
    response = client.post(f"/{tablename}/{version}/name/{name}", json=data)
    print(f"Endpoint = /{tablename}/{version}/name/{name}")
    assert response.status_code == 409

# PUT Track by Id - PASS
@mark.order(9)
@mark.parametrize("tablename, version, record", 
    [param("tracks", "v1", 3504, id="Tracks")])
def test_putid_pass(tablename: str, version: str, record: int):
    data = {"TrackName": "Test Track 3",
            "AlbumId": 1,
            "MediaTypeId": 1,
            "GenreId": 12,
            "Composer": "Some Random Dude",
            "Milliseconds": 123456,
            "Bytes": 9876543,
            "UnitPrice": 0.99
            }
    response = client.put(f"/{tablename}/{version}/id/{record}", json=data)
    print(f"Endpoint = /{tablename}/{version}/id/{record}")
    assert response.status_code == 201
    
# PUT Track by Id - FAIL
@mark.order(10)
@mark.parametrize("tablename, version, record", 
    [param("tracks", "v1", 9999, id="Tracks")])
def test_putid_fail(tablename: str, version: str, record: int):
    data = {"TrackName": "Test Track 3",
            "AlbumId": 1,
            "MediaTypeId": 1,
            "GenreId": 12,
            "Composer": "Some Random Dude",
            "Milliseconds": 123456,
            "Bytes": 9876543,
            "UnitPrice": 0.99
            }
    response = client.put(f"/{tablename}/{version}/id/{record}", json=data)
    print(f"Endpoint = /{tablename}/{version}/id/{record}")
    assert response.status_code == 404
    
# PUT Track by Name - PASS
@mark.order(11)
@mark.parametrize("tablename, version, name", 
    [param("tracks", "v1", "Test Track 3", id="Tracks")])
def test_putname_pass(tablename: str, version: str, name: str):
    data = {"TrackName": "Test Track 1",
            "AlbumId": 1,
            "MediaTypeId": 1,
            "GenreId": 12,
            "Composer": "Some Random Dude",
            "Milliseconds": 123456,
            "Bytes": 9876543,
            "UnitPrice": 0.99
            }
    response = client.put(f"/{tablename}/{version}/name/{name}", json=data)
    print(f"Endpoint = /{tablename}/{version}/name/{name}")
    assert response.status_code == 201

# PUT Track by Name - FAIL
@mark.order(12)
@mark.parametrize("tablename, version, name", 
    [param("tracks", "v1", "Test Track 3", id="Tracks")])
def test_putname_fail(tablename: str, version: str, name: str):
    data = {"TrackName": "Test Track 3",
            "AlbumId": 1,
            "MediaTypeId": 1,
            "GenreId": 12,
            "Composer": "Some Random Dude",
            "Milliseconds": 123456,
            "Bytes": 9876543,
            "UnitPrice": 0.99
            }
    response = client.put(f"/{tablename}/{version}/name/{name}", json=data)
    print(f"Endpoint = /{tablename}/{version}/name/{name}")
    assert response.status_code == 404

# DELETE Track by Id - PASS
@mark.order(13)
@mark.parametrize("tablename, version, record", 
    [param("tracks", "v1" , 3504, id="Tracks")])
def test_deleteid_pass(tablename: str, version: str, record: int):
    response = client.delete(f"/{tablename}/{version}/id/{record}")
    print(f"Endpoint = /{tablename}/{version}/id/{record}")
    assert response.status_code == 202

# DELETE Track by Id - FAIL
@mark.order(14)
@mark.parametrize("tablename, version, record", 
    [param("tracks", "v1", 3504, id="Tracks")])
def test_deleteid_fail(tablename: str, version: str, record: int):
    response = client.delete(f"/{tablename}/{version}/id/{record}")
    print(f"Endpoint = /{tablename}/{version}/id/{record}")
    assert response.status_code == 404

# DELETE Track by Name - PASS
@mark.order(15)
@mark.parametrize("tablename, version, name", 
    [param("tracks", "v1", "Test Track%", id="Tracks")])
def test_deletename_pass(tablename: str, version: str, name: str):
    response = client.delete(f"/{tablename}/{version}/name/{name}")
    print(f"Endpoint = /{tablename}/{version}/name/{name}")
    assert response.status_code == 202

# DELETE Track by Name - FAIL
@mark.order(16)
@mark.parametrize("tablename, version, name", 
    [param("tracks", "v1", "Test Track%", id="Tracks")])
def test_deletename_fail(tablename: str, version: str, name: str):
    response = client.delete(f"/{tablename}/{version}/name/{name}")
    print(f"Endpoint = /{tablename}/{version}/name/{name}")
    assert response.status_code == 404