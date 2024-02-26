from random import randint
from fastapi.testclient import TestClient
from pytest import mark, param

from src.main import app

client = TestClient(app)

# GET all albums - PASS = 347
@mark.parametrize("tablename, record", [param("albums", 347, id="Albums")])
def test_getall_albums(tablename, record):
    response = client.get(f"/{tablename}")
    print(f"Endpoint = /{tablename} record count {record}")
    assert response.status_code == 200
    assert len(response.json()) == record

# GET RANDOM album by album id - PASS = 1
@mark.parametrize("tablename, record", [param("albums", 347, id="Albums")])
def test_getid_pass(tablename: str, record: int):
    x = randint(1, record)
    response = client.get(f"/{tablename}/id/{x}")
    print(f"Endpoint = /{tablename}/id/{x}")
    assert response.status_code == 200
    assert len(response.json()) == 1

# GET albums by id - FAIL = detail not found
@mark.parametrize("tablename, record", [param("albums", 999, id="Albums")])
def test_getid_fail(tablename: str, record: int):
    response = client.get(f"/{tablename}/id/{record}")
    print(f"Endpoint = /{tablename}/id/{record}")
    assert response.status_code == 404
    assert response.json() == {"detail": "Album 999 not found"}

# GET albums by name - PASS = single record
@mark.parametrize("tablename, name", [param("albums", "A Matter of Life and Death", id="Albums")])
def test_getname_pass1(tablename: str, name: str):
    response = client.get(f"/{tablename}/name/{name}")
    print(f"Endpoint = /{tablename}/name/{name}")
    assert response.status_code == 200
    assert response.json() == [
        {"AlbumTitle": "A Matter of Life and Death", "ArtistId": 90}
    ]

# GET albums by name - PASS = multiple records
@mark.parametrize("tablename, name", [param("albums", "A Real%", id="Albums")])
def test_getname_pass2(tablename: str, name: str):
    response = client.get(f"/{tablename}/name/{name}")
    print(f"Endpoint = /{tablename}/name/{name}")
    assert response.status_code == 200
    assert response.json() == [
        {"AlbumTitle": "A Real Dead One", "ArtistId": 90},
        {"AlbumTitle": "A Real Live One", "ArtistId": 90},
    ]

# GET albums by name - FAIL = detail not found
@mark.parametrize("tablename, name", [param("albums", "Not Found", id="Albums")])
def test_getname_fail(tablename: str, name: str):
    response = client.get(f"/{tablename}/name/{name}")
    print(f"Endpoint = /{tablename}/name/{name}")
    assert response.status_code == 404
    assert response.json() == {"detail": "Album Not Found not found"}

# GET RANDOM album by artist id - one or more record(s)
@mark.parametrize("tablename, record", [param("albums", 347, id="Albums")])
def test_getartist_pass(tablename: str, record: int):
    x = randint(1, record)
    response = client.get(f"/{tablename}/artist/{x}")
    print(f"Endpoint = /{tablename}/artist/{x}")
    assert response.status_code == 200
    assert len(response.json()) >= 1

# GET album by artist id - FAIL - detail not found
@mark.parametrize("tablename, record", [param("albums", 999, id="Albums")])
def test_getartist_fail(tablename: str, record: int):
    response = client.get(f"/{tablename}/artist/{record}")
    print(f"Endpoint = /{tablename}/artist/{record}")
    assert response.status_code == 404
    assert response.json() == {"detail": "Album Not Found not found"} # TODO Change this

# POST test data by name - PASS
# POST test by name - FAIL

# POST album test data by JSON  - PASS
@mark.parametrize("tablename", [param("albums", id="Albums")])
def test_postalbum_pass1(tablename: str):
    data = [{"AlbumTitle": "Test Album", "ArtistId": 1}]
    response = client.post(f"/{tablename}/json", json=data)
    print(f"Endpoint = /{tablename}/json/{data}")
    assert response.status_code == 201

# POST album test data by JSON - PASS - UNIQUE constraint AlbumId & ArtistId
@mark.parametrize("tablename", [param("albums", id="Albums")])
def test_postalbum_pass2(tablename: str):
    data = [{"AlbumTitle": "Test Album", "ArtistId": 2}]
    response = client.post(f"/{tablename}/json", json=data)
    print(f"Endpoint = /{tablename}/json/{data}")
    assert response.status_code == 201
    assert response.json() == [
        {"accepted": [{"AlbumTitle": "Test Album", "ArtistId": 2}], "rejected": []}
        ]

# POST album test data by JSON - FAIL -  duplicate record
@mark.parametrize("tablename", [param("albums", id="Albums")])
def test_postalbum_fail(tablename: str):
    data = [{"AlbumTitle": "Test Album", "ArtistId": 1}]
    response = client.post(f"/{tablename}/json", json=data)
    print(f"Endpoint = /{tablename}/json/{data}")
    assert response.status_code == 201
    assert response.json() == [
        {"accepted": [], "rejected": [{"AlbumTitle": "Test Album", "ArtistId": 1}]}
        ]

# PUT album test data by Id - PASS
# PUT album test data by name - PASS
# PUT album test data by JSON - PASS
# PUT album test data by Id - FAIL
# PUT album test data by name - FAIL
# PUT album test data by JSON - FAIL

# DELETE album test data by Id - PASS
# DELETE album test data by name - PASS
# DELETE album test data by JSON - PASS
# DELETE album test data by Id - FAIL
# DELETE album test data by name - FAIL
# DELETE album test data by JSON - FAIL