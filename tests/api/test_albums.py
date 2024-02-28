from random import randint
from fastapi.testclient import TestClient
from pytest import mark, param

from src.main import app

client = TestClient(app)

# GET all albums - PASS - Records = 347
@mark.parametrize("tablename, record", [param("albums", 347, id="Albums")])
def test_getall_albums(tablename, record):
    response = client.get(f"/{tablename}")
    print(f"Endpoint = /{tablename} record count {record}")
    assert response.status_code == 200
    assert len(response.json()) == record

# GET RANDOM album by album id - PASS - One record
@mark.parametrize("tablename, record", [param("albums", 347, id="Albums")])
def test_getid_pass(tablename: str, record: int):
    x = randint(1, record)
    response = client.get(f"/{tablename}/id/{x}")
    print(f"Endpoint = /{tablename}/id/{x}")
    assert response.status_code == 200
    assert len(response.json()) == 1

# GET albums by id - FAIL - Detail not found
@mark.parametrize("tablename, record", [param("albums", 999, id="Albums")])
def test_getid_fail(tablename: str, record: int):
    response = client.get(f"/{tablename}/id/{record}")
    print(f"Endpoint = /{tablename}/id/{record}")
    assert response.status_code == 404
    assert response.json() == {"detail": "Album 999 not found"}

# GET albums by name - PASS - Single record
@mark.parametrize("tablename, name", [param("albums", "A Matter of Life and Death", id="Albums")])
def test_getname_pass1(tablename: str, name: str):
    response = client.get(f"/{tablename}/name/{name}")
    print(f"Endpoint = /{tablename}/name/{name}")
    assert response.status_code == 200
    assert response.json() == [{"AlbumTitle": "A Matter of Life and Death", "ArtistId": 90}]

# GET albums by name - PASS - Multiple records
@mark.parametrize("tablename, name", [param("albums", "A Real%", id="Albums")])
def test_getname_pass2(tablename: str, name: str):
    response = client.get(f"/{tablename}/name/{name}")
    print(f"Endpoint = /{tablename}/name/{name}")
    assert response.status_code == 200
    assert response.json() == [
        {"AlbumTitle": "A Real Dead One", "ArtistId": 90},
        {"AlbumTitle": "A Real Live One", "ArtistId": 90},
    ]

# GET albums by name - FAIL - Detail not found
@mark.parametrize("tablename, name", [param("albums", "Not Found", id="Albums")])
def test_getname_fail(tablename: str, name: str):
    response = client.get(f"/{tablename}/name/{name}")
    print(f"Endpoint = /{tablename}/name/{name}")
    assert response.status_code == 404
    assert response.json() == {"detail": "Album Not Found not found"}

# GET RANDOM album by artist id - One or more record(s)
@mark.parametrize("tablename, record", [param("albums", 275, id="Albums")])
def test_getartist_pass(tablename: str, record: int):
    x = randint(1, record)
    response = client.get(f"/{tablename}/artist/{x}")
    print(f"Endpoint = /{tablename}/artist/{x}")
    assert response.status_code == 200
    assert len(response.json()) >= 1

# GET album by artist id - FAIL - Detail not found
@mark.parametrize("tablename, record", [param("albums", 999, id="Albums")])
def test_getartist_fail(tablename: str, record: int):
    response = client.get(f"/{tablename}/artist/{record}")
    print(f"Endpoint = /{tablename}/artist/{record}")
    assert response.status_code == 404
    assert response.json() == {"detail": "Artist Id 999 not found"}

# POST test data by name - PASS - New record
@mark.parametrize("tablename, name", [param("albums", "name", id="Albums")])
def test_postname_pass1(tablename: str, name: str):
    data = {"AlbumTitle": "Test Album", "ArtistId": 1}
    response = client.post(f"/{tablename}/name/{name}", json=data)
    print(f"Endpoint = /{tablename}/name/{name}")
    assert response.status_code == 201
    assert response.json() == {"AlbumTitle": "Test Album", "ArtistId": 1}
    
# POST test data by name - PASS - UNIQUE contraint
@mark.parametrize("tablename, name", [param("albums", "name", id="Albums")])
def test_postname_pass2(tablename: str, name: str):
    data = {"AlbumTitle": "Test Album", "ArtistId": 2}
    response = client.post(f"/{tablename}/name/{name}", json=data)
    print(f"Endpoint = /{tablename}/name/{name}")
    assert response.status_code == 201
    assert response.json() == {"AlbumTitle": "Test Album", "ArtistId": 2}

# POST test by name - FAIL - Duplicate record
@mark.parametrize("tablename, name", [param("albums", "name", id="Albums")])
def test_postname_fail1(tablename: str, name: str):
    data = {"AlbumTitle": "Test Album", "ArtistId": 1}
    response = client.post(f"/{tablename}/name/{name}", json=data)
    print(f"Endpoint = /{tablename}/name/{name}")
    assert response.status_code == 409
    assert response.json() == {"detail":"Album AlbumTitle='Test Album' ArtistId=1 already exists"}

# POST test by name - FAIL - Unknown ArtistId
@mark.parametrize("tablename, name", [param("albums", "name", id="Albums")])
def test_postname_fail2(tablename: str, name: str):
    data = {"AlbumTitle": "Test Album", "ArtistId": 999}
    response = client.post(f"/{tablename}/name/{name}", json=data)
    print(f"Endpoint = /{tablename}/name/{name}")
    assert response.status_code == 500
    assert response.json() == {"detail":"Database Error. Please check application logs"}

# PUT album test data by id - PASS - AlbumTitle
@mark.parametrize("tablename, record", [param("albums", 348, id="Albums")])
def test_putid_pass1(tablename: str, record: int):
    data = {"AlbumTitle": "Another Test Album", "ArtistId": 1}
    response = client.put(f"/{tablename}/id/{record}", json=data)
    print(f"Endpoint = /{tablename}/name/{record}")
    assert response.status_code == 201
    assert response.json() == {"AlbumTitle": "Another Test Album","ArtistId": 1}
    
# PUT album test data by id - PASS - ArtistId
@mark.parametrize("tablename, record", [param("albums", 348, id="Albums")])
def test_putid_pass2(tablename: str, record: int):
    data = {"AlbumTitle": "Another Test Album", "ArtistId": 2}
    response = client.put(f"/{tablename}/id/{record}", json=data)
    print(f"Endpoint = /{tablename}/id/{record}")
    assert response.status_code == 201
    assert response.json() == {"AlbumTitle": "Another Test Album","ArtistId": 2}

# PUT album test data by id - FAIL - Unknown Id
@mark.parametrize("tablename, record", [param("albums", 999, id="Albums")])
def test_putid_fail1(tablename: str, record: int):
    data = {"AlbumTitle": "Another Test Album", "ArtistId": 1}
    response = client.put(f"/{tablename}/id/{record}", json=data)
    print(f"Endpoint = /{tablename}/id/{record}")
    assert response.status_code == 404
    assert response.json() == {"detail": "Album 999 not found"}
    
# PUT album test data by id - FAIL - Unknown ArtistId
@mark.parametrize("tablename, record", [param("albums", 348, id="Albums")])
def test_putid_fail2(tablename: str, record: int):
    data = {"AlbumTitle": "Another Test Album", "ArtistId": 999}
    response = client.put(f"/{tablename}/id/{record}", json=data)
    print(f"Endpoint = /{tablename}/id/{record}")
    assert response.status_code == 500
    assert response.json() == {"detail": "Database Error. Please check application logs"}

# PUT album test data by name - PASS - AlbumTitle
@mark.parametrize("tablename, name", [param("albums", "Another Test Album", id="Albums")])
def test_putname_pass1(tablename: str, name: str):
    data = {"AlbumTitle": "Test Album","ArtistId": 1}
    response = client.put(f"/{tablename}/name/{name}", json=data)
    print(f"Endpoint = /{tablename}/name/{name}")
    assert response.status_code == 201
    assert response.json() == {"AlbumTitle": "Test Album","ArtistId": 1}

# PUT album test data by name - PASS - ArtistId
@mark.parametrize("tablename, name", [param("albums", "Test Album", id="Albums")])
def test_putname_pass2(tablename: str, name: str):
    data = {"AlbumTitle": "More Test Albums","ArtistId": 1}
    response = client.put(f"/{tablename}/name/{name}", json=data)
    print(f"Endpoint = /{tablename}/name/{name}")
    assert response.status_code == 201
    assert response.json() == {"AlbumTitle": "More Test Albums","ArtistId": 1}

# PUT album test data by name - FAIL - Unknown ArtistId
@mark.parametrize("tablename, name", [param("albums", "Test Album", id="Albums")])
def test_putname_fail(tablename: str, name: str):
    data = {"AlbumTitle": "More Test Albums","ArtistId": 999}
    response = client.put(f"/{tablename}/name/{name}", json=data)
    print(f"Endpoint = /{tablename}/name/{name}")
    assert response.status_code == 500
    assert response.json() == {"detail": "Database Error. Please check application logs"}

# DELETE album test data by id - PASS
@mark.parametrize("tablename, record", [param("albums", 348, id="Albums")])
def test_deleteid_pass(tablename: str, record: int):
    response = client.delete(f"/{tablename}/id/{record}")
    print(f"Endpoint = /{tablename}/id/{record}")
    assert response.status_code == 202
    assert response.json() == [{"Id": 348, "AlbumTitle": "More Test Albums", "ArtistId": 1}]

# DELETE album test data by id - FAIL - Unknown Id
@mark.parametrize("tablename, record", [param("albums", 348, id="Albums")])
def test_deleteid_fail(tablename: str, record: int):
    response = client.delete(f"/{tablename}/id/{record}")
    print(f"Endpoint = /{tablename}/id/{record}")
    assert response.status_code == 404
    assert response.json() == {"detail": "Album 348 not found"}

# DELETE album test data by name - PASS
@mark.parametrize("tablename, name", [param("albums", "Test Album", id="Albums")])
def test_deletename_pass(tablename: str, name: str):
    response = client.delete(f"/{tablename}/name/{name}")
    print(f"Endpoint = /{tablename}/name/{name}")
    assert response.status_code == 202
    assert response.json() == [{"Id": 349,"AlbumTitle": "Test Album","ArtistId": 2}]

# DELETE album test data by name - FAIL - Not Found
@mark.parametrize("tablename, name", [param("albums", "Test Album", id="Albums")])
def test_deletename_fail(tablename: str, name: str):
    response = client.delete(f"/{tablename}/name/{name}")
    print(f"Endpoint = /{tablename}/name/{name}")
    assert response.status_code == 404
    assert response.json() == {"detail": "Album Test Album not found"}