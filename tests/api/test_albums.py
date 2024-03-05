from random import randint
from fastapi.testclient import TestClient
from pytest import mark, param

from src.main import app

client = TestClient(app)

# GET All Albums - PASS - Records = 347
@mark.order(1)
@mark.parametrize("tablename, version, record", 
    [param("albums", "v1", 347, id="Albums")])
def test_getall_albums(tablename: str, version: str, record: int):
    response = client.get(f"/{tablename}/{version}")
    print(f"Endpoint = /{tablename}/{version} record count {record}")
    assert response.status_code == 200
    assert len(response.json()) == record

# GET RANDOM Album by Album Id - PASS - One record
@mark.order(2)
@mark.parametrize("tablename, version, record", 
    [param("albums", "v1", 347, id="Albums")])
def test_getid_pass(tablename: str, version: str, record: int):
    x = randint(1, record)
    response = client.get(f"/{tablename}/{version}/id/{x}")
    print(f"Endpoint = /{tablename}/{version}/id/{x}")
    assert response.status_code == 200
    assert len(response.json()) == 1

# GET Albums by Id - FAIL - Detail not found
@mark.order(3)
@mark.parametrize("tablename, version, record", 
    [param("albums", "v1", 999, id="Albums")])
def test_getid_fail(tablename: str, version: str, record: int):
    response = client.get(f"/{tablename}/{version}/id/{record}")
    print(f"Endpoint = /{tablename}/{version}/id/{record}")
    assert response.status_code == 404

# GET Albums by Name - PASS - Single record
@mark.order(8)
@mark.parametrize("tablename, version, name", 
    [param("albums", "v1", "Test Album", id="Albums")])
def test_getname_pass1(tablename: str, version: str, name: str):
    response = client.get(f"/{tablename}/{version}/name/{name}")
    print(f"Endpoint = /{tablename}/{version}/name/{name}")
    assert response.status_code == 200

# GET Albums by Name - PASS - Multiple records
@mark.order(10)
@mark.parametrize("tablename, version, name", 
    [param("albums", "v1", "Test%", id="Albums")])
def test_getname_pass2(tablename: str, version: str, name: str):
    response = client.get(f"/{tablename}/{version}/name/{name}")
    print(f"Endpoint = /{tablename}/{version}/name/{name}")
    assert response.status_code == 200
    
# GET Albums by Name - FAIL - Detail not found
@mark.order(4)
@mark.parametrize("tablename, version, name", 
    [param("albums", "v1", "Not Found", id="Albums")])
def test_getname_fail(tablename: str, version: str, name: str):
    response = client.get(f"/{tablename}/{version}/name/{name}")
    print(f"Endpoint = /{tablename}/{version}/name/{name}")
    assert response.status_code == 404

# GET RANDOM Album by Artist Id - One or more record(s)
@mark.order(5)
@mark.parametrize("tablename, version, record", 
    [param("albums", "v1", 275, id="Albums")])
def test_getartist_pass(tablename: str, version: str, record: int):
    # TODO Intermittent failure ArtistId - Best of Three?
    x = randint(1, record)
    response = client.get(f"/{tablename}/{version}/artist/{x}")
    print(f"Endpoint = /{tablename}/{version}/artist/{x}")
    assert response.status_code == 200
    assert len(response.json()) >= 1

# GET Album by Artist Id - FAIL - Detail not found
@mark.order(6)
@mark.parametrize("tablename, version, record", 
    [param("albums", "v1", 999, id="Albums")])
def test_getartist_fail(tablename: str, version: str, record: int):
    response = client.get(f"/{tablename}/{version}/artist/{record}")
    print(f"Endpoint = /{tablename}/{version}/artist/{record}")
    assert response.status_code == 404
    
# POST Test Data by Name - PASS - New record
@mark.order(7)
@mark.parametrize("tablename, version, name", 
    [param("albums", "v1", "name", id="Albums")])
def test_postname_pass1(tablename: str, version: str, name: str):
    data = {"AlbumTitle":"Test Album", "ArtistId": 1}
    response = client.post(f"/{tablename}/{version}/name/{name}", json=data)
    print(f"Endpoint = /{tablename}/{version}/name/{name}")
    assert response.status_code == 201

# POST Test Data by Name - PASS - UNIQUE contraint
@mark.order(9)
@mark.parametrize("tablename, version, name", 
    [param("albums", "v1", "name", id="Albums")])
def test_postname_pass2(tablename: str, version: str, name: str):
    data = {"AlbumTitle":"Test Album", "ArtistId": 2}
    response = client.post(f"/{tablename}/{version}/name/{name}", json=data)
    print(f"Endpoint = /{tablename}/{version}/name/{name}")
    assert response.status_code == 201

# POST Test by Name - FAIL - Duplicate record
@mark.order(11)
@mark.parametrize("tablename, version, name", 
    [param("albums", "v1", "name", id="Albums")])
def test_postname_fail1(tablename: str, version: str, name: str):
    data = {"AlbumTitle":"Test Album", "ArtistId": 1}
    response = client.post(f"/{tablename}/{version}/name/{name}", json=data)
    print(f"Endpoint = /{tablename}/{version}/name/{name}")
    assert response.status_code == 409

# POST Test by Name - FAIL - Unknown ArtistId
@mark.order(12)
@mark.parametrize("tablename, version, name", 
    [param("albums", "v1", "name", id="Albums")])
def test_postname_fail2(tablename: str, version: str, name: str):
    data = {"AlbumTitle":"Test Album", "ArtistId": 999}
    response = client.post(f"/{tablename}/{version}/name/{name}", json=data)
    print(f"Endpoint = /{tablename}/{version}/name/{name}")
    assert response.status_code == 500

# PUT Album Test Data by Id - PASS - AlbumTitle
@mark.order(13)
@mark.parametrize("tablename, version, record", 
    [param("albums", "v1", 348, id="Albums")])
def test_putid_pass1(tablename: str, version: str, record: int):
    data = {"AlbumTitle":"Another Test Album", "ArtistId": 1}
    response = client.put(f"/{tablename}/{version}/id/{record}", json=data)
    print(f"Endpoint = /{tablename}/{version}/name/{record}")
    assert response.status_code == 201
    
# PUT Album Test Data by Id - PASS - ArtistId
@mark.order(14)
@mark.parametrize("tablename, version, record", 
    [param("albums", "v1", 348, id="Albums")])
def test_putid_pass2(tablename: str, version: str, record: int):
    data = {"AlbumTitle":"Another Test Album", "ArtistId": 2}
    response = client.put(f"/{tablename}/{version}/id/{record}", json=data)
    print(f"Endpoint = /{tablename}/{version}/id/{record}")
    assert response.status_code == 201

# PUT Album Test Data by Id - FAIL - Unknown Id
@mark.order(15)
@mark.parametrize("tablename, version, record", 
    [param("albums", "v1", 999, id="Albums")])
def test_putid_fail1(tablename: str, version: str, record: int):
    data = {"AlbumTitle":"Another Test Album", "ArtistId": 1}
    response = client.put(f"/{tablename}/{version}/id/{record}", json=data)
    print(f"Endpoint = /{tablename}/{version}/id/{record}")
    assert response.status_code == 404
    
# PUT Album Test Data by Id - FAIL - Unknown ArtistId
@mark.order(16)
@mark.parametrize("tablename, version, record", 
    [param("albums", "v1", 348, id="Albums")])
def test_putid_fail2(tablename: str, version: str, record: int):
    data = {"AlbumTitle":"Another Test Album", "ArtistId": 999}
    response = client.put(f"/{tablename}/{version}/id/{record}", json=data)
    print(f"Endpoint = /{tablename}/{version}/id/{record}")
    assert response.status_code == 500

# PUT Album Test Data by Name - PASS - AlbumTitle
@mark.order(17)
@mark.parametrize("tablename, version, name", 
    [param("albums", "v1", "Another Test Album", id="Albums")])
def test_putname_pass1(tablename: str, version: str, name: str):
    data = {"AlbumTitle":"Test Album", "ArtistId": 1}
    response = client.put(f"/{tablename}/{version}/name/{name}", json=data)
    print(f"Endpoint = /{tablename}/{version}/name/{name}")
    assert response.status_code == 201

# PUT Album Test Data by Name - PASS - ArtistId
@mark.order(18)
@mark.parametrize("tablename, version, name", 
    [param("albums", "v1", "Test Album", id="Albums")])
def test_putname_pass2(tablename: str, version: str, name: str):
    data = {"AlbumTitle":"More Test Albums", "ArtistId": 1}
    response = client.put(f"/{tablename}/{version}/name/{name}", json=data)
    print(f"Endpoint = /{tablename}/{version}/name/{name}")
    assert response.status_code == 201

# PUT Album Test Data by Name - FAIL - Unknown ArtistId
@mark.order(19)
@mark.parametrize("tablename, version, name", 
    [param("albums", "v1", "Test Album", id="Albums")])
def test_putname_fail(tablename: str, version: str, name: str):
    data = {"AlbumTitle":"More Test Albums", "ArtistId": 999}
    response = client.put(f"/{tablename}/{version}/name/{name}", json=data)
    print(f"Endpoint = /{tablename}/{version}/name/{name}")
    assert response.status_code == 500

# DELETE Album Test Data by Id - PASS
@mark.order(20)
@mark.parametrize("tablename, version, record", 
    [param("albums", "v1" , 348, id="Albums")])
def test_deleteid_pass(tablename: str, version: str, record: int):
    response = client.delete(f"/{tablename}/{version}/id/{record}")
    print(f"Endpoint = /{tablename}/{version}/id/{record}")
    assert response.status_code == 202

# DELETE Album Test Data by Id - FAIL - Unknown Id
@mark.order(21)
@mark.parametrize("tablename, version, record", 
    [param("albums", "v1", 348, id="Albums")])
def test_deleteid_fail(tablename: str, version: str, record: int):
    response = client.delete(f"/{tablename}/{version}/id/{record}")
    print(f"Endpoint = /{tablename}/{version}/id/{record}")
    assert response.status_code == 404

# DELETE Album Test Data by Name - PASS
@mark.order(22)
@mark.parametrize("tablename, version, name", 
    [param("albums", "v1", "Test Album", id="Albums")])
def test_deletename_pass(tablename: str, version: str, name: str):
    response = client.delete(f"/{tablename}/{version}/name/{name}")
    print(f"Endpoint = /{tablename}/{version}/name/{name}")
    assert response.status_code == 202

# DELETE Album Test Data by Name - FAIL - Not Found
@mark.order(23)
@mark.parametrize("tablename, version, name", 
    [param("albums", "v1", "Test Album", id="Albums")])
def test_deletename_fail(tablename: str, version: str, name: str):
    response = client.delete(f"/{tablename}/{version}/name/{name}")
    print(f"Endpoint = /{tablename}/{version}/name/{name}")
    assert response.status_code == 404