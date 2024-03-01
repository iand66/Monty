from random import randint
from fastapi.testclient import TestClient
from pytest import mark, param

from src.main import app

client = TestClient(app)

# GET all albums - PASS - Records = 347
@mark.parametrize("tablename, version, record", 
    [param("albums", "v1", 347, id="Albums")])
def test_getall_albums(tablename: str, version: str, record: int):
    response = client.get(f"/{tablename}/{version}")
    print(f"Endpoint = /{tablename}/{version} record count {record}")
    assert response.status_code == 200
    assert len(response.json()) == record

# GET RANDOM album by album id - PASS - One record
@mark.parametrize("tablename, version, record", 
    [param("albums", "v1", 347, id="Albums")])
def test_getid_pass(tablename: str, version: str, record: int):
    x = randint(1, record)
    response = client.get(f"/{tablename}/{version}/id/{x}")
    print(f"Endpoint = /{tablename}/{version}/id/{x}")
    assert response.status_code == 200
    assert len(response.json()) == 1

# GET albums by id - FAIL - Detail not found
@mark.parametrize("tablename, version, record", 
    [param("albums", "v1", 999, id="Albums")])
def test_getid_fail(tablename: str, version: str, record: int):
    response = client.get(f"/{tablename}/{version}/id/{record}")
    print(f"Endpoint = /{tablename}/{version}/id/{record}")
    assert response.status_code == 404
    assert response.json() == {"detail": "Album 999 not found"}

# GET albums by name - PASS - Single record
@mark.parametrize("tablename, version, name", 
    [param("albums", "v1", "A Matter of Life and Death", id="Albums")])
def test_getname_pass1(tablename: str, version: str, name: str):
    response = client.get(f"/{tablename}/{version}/name/{name}")
    print(f"Endpoint = /{tablename}/{version}/name/{name}")
    assert response.status_code == 200
    assert response.json() == [{"AlbumTitle": "A Matter of Life and Death", "ArtistId": 90}]

# GET albums by name - PASS - Multiple records
@mark.parametrize("tablename, version, name", 
    [param("albums", "v1", "A Real%", id="Albums")])
def test_getname_pass2(tablename: str, version: str, name: str):
    response = client.get(f"/{tablename}/{version}/name/{name}")
    print(f"Endpoint = /{tablename}/{version}/name/{name}")
    assert response.status_code == 200
    assert response.json() == [
        {"AlbumTitle": "A Real Dead One", "ArtistId": 90},
        {"AlbumTitle": "A Real Live One", "ArtistId": 90},
    ]

# GET albums by name - FAIL - Detail not found
@mark.parametrize("tablename, version, name", 
    [param("albums", "v1", "Not Found", id="Albums")])
def test_getname_fail(tablename: str, version: str, name: str):
    response = client.get(f"/{tablename}/{version}/name/{name}")
    print(f"Endpoint = /{tablename}/{version}/name/{name}")
    assert response.status_code == 404
    assert response.json() == {"detail": "Album Not Found not found"}

# GET RANDOM album by artist id - One or more record(s)
# TODO Intermittent failure ArtistId - Best of Three?
@mark.parametrize("tablename, version, record", 
    [param("albums", "v1", 275, id="Albums")])
def test_getartist_pass(tablename: str, version: str, record: int):
    x = randint(1, record)
    response = client.get(f"/{tablename}/{version}/artist/{x}")
    print(f"Endpoint = /{tablename}/{version}/artist/{x}")
    assert response.status_code == 200
    assert len(response.json()) >= 1

# GET album by artist id - FAIL - Detail not found
@mark.parametrize("tablename, version, record", 
    [param("albums", "v1", 999, id="Albums")])
def test_getartist_fail(tablename: str, version: str, record: int):
    response = client.get(f"/{tablename}/{version}/artist/{record}")
    print(f"Endpoint = /{tablename}/{version}/artist/{record}")
    assert response.status_code == 404
    assert response.json() == {"detail": "Artist Id 999 not found"}

# POST test data by name - PASS - New record
@mark.parametrize("tablename, version, name", 
    [param("albums", "v1", "name", id="Albums")])
def test_postname_pass1(tablename: str, version: str, name: str):
    data = {"AlbumTitle": "Test Album", "ArtistId": 1}
    response = client.post(f"/{tablename}/{version}/name/{name}", json=data)
    print(f"Endpoint = /{tablename}/{version}/name/{name}")
    assert response.status_code == 201
    assert response.json() == {"AlbumTitle": "Test Album", "ArtistId": 1}
    
# POST test data by name - PASS - UNIQUE contraint
@mark.parametrize("tablename, version, name", 
    [param("albums", "v1", "name", id="Albums")])
def test_postname_pass2(tablename: str, version: str, name: str):
    data = {"AlbumTitle": "Test Album", "ArtistId": 2}
    response = client.post(f"/{tablename}/{version}/name/{name}", json=data)
    print(f"Endpoint = /{tablename}/{version}/name/{name}")
    assert response.status_code == 201
    assert response.json() == {"AlbumTitle": "Test Album", "ArtistId": 2}

# POST test by name - FAIL - Duplicate record
@mark.parametrize("tablename, version, name", 
    [param("albums", "v1", "name", id="Albums")])
def test_postname_fail1(tablename: str, version: str, name: str):
    data = {"AlbumTitle": "Test Album", "ArtistId": 1}
    response = client.post(f"/{tablename}/{version}/name/{name}", json=data)
    print(f"Endpoint = /{tablename}/{version}/name/{name}")
    assert response.status_code == 409
    assert response.json() == {"detail":"Album AlbumTitle='Test Album' ArtistId=1 already exists"}

# POST test by name - FAIL - Unknown ArtistId
@mark.parametrize("tablename, version, name", 
    [param("albums", "v1", "name", id="Albums")])
def test_postname_fail2(tablename: str, version: str, name: str):
    data = {"AlbumTitle": "Test Album", "ArtistId": 999}
    response = client.post(f"/{tablename}/{version}/name/{name}", json=data)
    print(f"Endpoint = /{tablename}/{version}/name/{name}")
    assert response.status_code == 500
    assert response.json() == {"detail":"Database Error. Please check application logs"}

# PUT album test data by id - PASS - AlbumTitle
@mark.parametrize("tablename, version, record", 
    [param("albums", "v1", 348, id="Albums")])
def test_putid_pass1(tablename: str, version: str, record: int):
    data = {"AlbumTitle": "Another Test Album", "ArtistId": 1}
    response = client.put(f"/{tablename}/{version}/id/{record}", json=data)
    print(f"Endpoint = /{tablename}/{version}/name/{record}")
    assert response.status_code == 201
    assert response.json() == {"AlbumTitle": "Another Test Album","ArtistId": 1}
    
# PUT album test data by id - PASS - ArtistId
@mark.parametrize("tablename, version, record", 
    [param("albums", "v1", 348, id="Albums")])
def test_putid_pass2(tablename: str, version: str, record: int):
    data = {"AlbumTitle": "Another Test Album", "ArtistId": 2}
    response = client.put(f"/{tablename}/{version}/id/{record}", json=data)
    print(f"Endpoint = /{tablename}/{version}/id/{record}")
    assert response.status_code == 201
    assert response.json() == {"AlbumTitle": "Another Test Album","ArtistId": 2}

# PUT album test data by id - FAIL - Unknown Id
@mark.parametrize("tablename, version, record", 
    [param("albums", "v1", 999, id="Albums")])
def test_putid_fail1(tablename: str, version: str, record: int):
    data = {"AlbumTitle": "Another Test Album", "ArtistId": 1}
    response = client.put(f"/{tablename}/{version}/id/{record}", json=data)
    print(f"Endpoint = /{tablename}/{version}/id/{record}")
    assert response.status_code == 404
    assert response.json() == {"detail": "Album 999 not found"}
    
# PUT album test data by id - FAIL - Unknown ArtistId
@mark.parametrize("tablename, version, record", 
    [param("albums", "v1", 348, id="Albums")])
def test_putid_fail2(tablename: str, version: str, record: int):
    data = {"AlbumTitle": "Another Test Album", "ArtistId": 999}
    response = client.put(f"/{tablename}/{version}/id/{record}", json=data)
    print(f"Endpoint = /{tablename}/{version}/id/{record}")
    assert response.status_code == 500
    assert response.json() == {"detail": "Database Error. Please check application logs"}

# PUT album test data by name - PASS - AlbumTitle
@mark.parametrize("tablename, version, name", 
    [param("albums", "v1","Another Test Album", id="Albums")])
def test_putname_pass1(tablename: str, version: str, name: str):
    data = {"AlbumTitle": "Test Album","ArtistId": 1}
    response = client.put(f"/{tablename}/{version}/name/{name}", json=data)
    print(f"Endpoint = /{tablename}/{version}/name/{name}")
    assert response.status_code == 201
    assert response.json() == {"AlbumTitle": "Test Album","ArtistId": 1}

# PUT album test data by name - PASS - ArtistId
@mark.parametrize("tablename, version, name", 
    [param("albums", "v1" ,"Test Album", id="Albums")])
def test_putname_pass2(tablename: str, version: str, name: str):
    data = {"AlbumTitle": "More Test Albums","ArtistId": 1}
    response = client.put(f"/{tablename}/{version}/name/{name}", json=data)
    print(f"Endpoint = /{tablename}/{version}/name/{name}")
    assert response.status_code == 201
    assert response.json() == {"AlbumTitle": "More Test Albums","ArtistId": 1}

# PUT album test data by name - FAIL - Unknown ArtistId
@mark.parametrize("tablename, version, name", 
    [param("albums", "v1", "Test Album", id="Albums")])
def test_putname_fail(tablename: str, version: str, name: str):
    data = {"AlbumTitle": "More Test Albums","ArtistId": 999}
    response = client.put(f"/{tablename}/{version}/name/{name}", json=data)
    print(f"Endpoint = /{tablename}/{version}/name/{name}")
    assert response.status_code == 500
    assert response.json() == {"detail": "Database Error. Please check application logs"}

# DELETE album test data by id - PASS
@mark.parametrize("tablename, version, record", 
    [param("albums", "v1" , 348, id="Albums")])
def test_deleteid_pass(tablename: str, version: str, record: int):
    response = client.delete(f"/{tablename}/{version}/id/{record}")
    print(f"Endpoint = /{tablename}/{version}/id/{record}")
    assert response.status_code == 202
    assert response.json() == [{"Id": 348, "AlbumTitle": "More Test Albums", "ArtistId": 1}]

# DELETE album test data by id - FAIL - Unknown Id
@mark.parametrize("tablename, version, record", 
    [param("albums", "v1", 348, id="Albums")])
def test_deleteid_fail(tablename: str, version: str, record: int):
    response = client.delete(f"/{tablename}/{version}/id/{record}")
    print(f"Endpoint = /{tablename}/{version}/id/{record}")
    assert response.status_code == 404
    assert response.json() == {"detail": "Album 348 not found"}

# DELETE album test data by name - PASS
@mark.parametrize("tablename, version, name", 
    [param("albums", "v1", "Test Album", id="Albums")])
def test_deletename_pass(tablename: str, version: str, name: str):
    response = client.delete(f"/{tablename}/{version}/name/{name}")
    print(f"Endpoint = /{tablename}/{version}/name/{name}")
    assert response.status_code == 202
    assert response.json() == [{"Id": 349,"AlbumTitle": "Test Album","ArtistId": 2}]

# DELETE album test data by name - FAIL - Not Found
@mark.parametrize("tablename, version, name", 
    [param("albums", "v1", "Test Album", id="Albums")])
def test_deletename_fail(tablename: str, version: str, name: str):
    response = client.delete(f"/{tablename}/{version}/name/{name}")
    print(f"Endpoint = /{tablename}/{version}/name/{name}")
    assert response.status_code == 404
    assert response.json() == {"detail": "Album Test Album not found"}