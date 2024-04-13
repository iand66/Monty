from random import randint

from fastapi.testclient import TestClient
from pytest import mark, param

from src.main import app

client = TestClient(app)


# GET All Albums - PASS
@mark.order(1)
@mark.parametrize(
    "tablename, version, record", [param("albums", "v1", 347, id="Albums")]
)
def test_getall(tablename: str, version: str, record: int):
    response = client.get(f"/{tablename}/{version}")
    print(f"Endpoint = /{tablename}/{version} records {record}")
    assert response.status_code == 200
    assert len(response.json()) == record


# GET RANDOM Album by Album Id - PASS
@mark.order(2)
@mark.parametrize(
    "tablename, version, record", [param("albums", "v1", 347, id="Albums")]
)
def test_getid_pass(tablename: str, version: str, record: int):
    x = randint(1, record)
    response = client.get(f"/{tablename}/{version}/id/{x}")
    print(f"Endpoint = /{tablename}/{version}/id/{x}")
    assert response.status_code == 200
    assert len(response.json()) == 1


# GET Albums by Id - FAIL
@mark.order(3)
@mark.parametrize(
    "tablename, version, record", [param("albums", "v1", 999, id="Albums")]
)
def test_getid_fail(tablename: str, version: str, record: int):
    response = client.get(f"/{tablename}/{version}/id/{record}")
    print(f"Endpoint = /{tablename}/{version}/id/{record}")
    assert response.status_code == 404


# GET Albums by Name - FAIL
@mark.order(4)
@mark.parametrize(
    "tablename, version, name", [param("albums", "v1", "Not Found", id="Albums")]
)
def test_getname_fail(tablename: str, version: str, name: str):
    response = client.get(f"/{tablename}/{version}/name/{name}")
    print(f"Endpoint = /{tablename}/{version}/name/{name}")
    assert response.status_code == 404


# GET RANDOM Album by Artist Id
@mark.order(5)
@mark.flaky(reruns=3, reason="Not all artists have albums")
@mark.parametrize(
    "tablename, version, record", [param("albums", "v1", 275, id="Albums")]
)
def test_getartist_pass(tablename: str, version: str, record: int):
    x = randint(1, record)
    response = client.get(f"/{tablename}/{version}/artist/{x}")
    print(f"Endpoint = /{tablename}/{version}/artist/{x}")
    assert response.status_code == 200
    assert len(response.json()) >= 1


# GET Album by Artist Id - FAIL
@mark.order(6)
@mark.parametrize(
    "tablename, version, record", [param("albums", "v1", 999, id="Albums")]
)
def test_getartist_fail(tablename: str, version: str, record: int):
    response = client.get(f"/{tablename}/{version}/artist/{record}")
    print(f"Endpoint = /{tablename}/{version}/artist/{record}")
    assert response.status_code == 404


# POST by Name - PASS
@mark.order(7)
@mark.parametrize(
    "tablename, version, name", [param("albums", "v1", "name", id="Albums")]
)
def test_postname_pass1(tablename: str, version: str, name: str):
    data = {"AlbumTitle": "Test Album", "ArtistId": 1}
    response = client.post(f"/{tablename}/{version}/name/{name}", json=data)
    print(f"Endpoint = /{tablename}/{version}/name/{name}")
    assert response.status_code == 201


# POST by Name - PASS
@mark.order(8)
@mark.parametrize(
    "tablename, version, name", [param("albums", "v1", "name", id="Albums")]
)
def test_postname_pass2(tablename: str, version: str, name: str):
    data = {"AlbumTitle": "Test Album", "ArtistId": 2}
    response = client.post(f"/{tablename}/{version}/name/{name}", json=data)
    print(f"Endpoint = /{tablename}/{version}/name/{name}")
    assert response.status_code == 201


# GET Albums by Name - PASS
@mark.order(9)
@mark.parametrize(
    "tablename, version, name", [param("albums", "v1", "Test Album", id="Albums")]
)
def test_getname_pass(tablename: str, version: str, name: str):
    response = client.get(f"/{tablename}/{version}/name/{name}")
    print(f"Endpoint = /{tablename}/{version}/name/{name}")
    assert response.status_code == 200


# POST by Name - FAIL
@mark.order(10)
@mark.parametrize(
    "tablename, version, name", [param("albums", "v1", "name", id="Albums")]
)
def test_postname_fail(tablename: str, version: str, name: str):
    data = {"AlbumTitle": "Test Album", "ArtistId": 1}
    response = client.post(f"/{tablename}/{version}/name/{name}", json=data)
    print(f"Endpoint = /{tablename}/{version}/name/{name}")
    assert response.status_code == 409


# PUT Album by Id - PASS
@mark.order(11)
@mark.parametrize(
    "tablename, version, record", [param("albums", "v1", 348, id="Albums")]
)
def test_putid_pass(tablename: str, version: str, record: int):
    data = {"AlbumTitle": "Another Test", "ArtistId": 1}
    response = client.put(f"/{tablename}/{version}/id/{record}", json=data)
    print(f"Endpoint = /{tablename}/{version}/id/{record}")
    assert response.status_code == 201


# PUT Album by Id - FAIL
@mark.order(12)
@mark.parametrize(
    "tablename, version, record", [param("albums", "v1", 999, id="Albums")]
)
def test_putid_fail(tablename: str, version: str, record: int):
    data = {"AlbumTitle": "Another Test", "ArtistId": 1}
    response = client.put(f"/{tablename}/{version}/id/{record}", json=data)
    print(f"Endpoint = /{tablename}/{version}/id/{record}")
    assert response.status_code == 404


# PUT Album by Name - PASS
@mark.order(13)
@mark.parametrize(
    "tablename, version, name", [param("albums", "v1", "Another Test", id="Albums")]
)
def test_putname_pass(tablename: str, version: str, name: str):
    data = {"AlbumTitle": "Test Album", "ArtistId": 1}
    response = client.put(f"/{tablename}/{version}/name/{name}", json=data)
    print(f"Endpoint = /{tablename}/{version}/name/{name}")
    assert response.status_code == 201


# PUT Album by Name - FAIL
@mark.order(14)
@mark.parametrize(
    "tablename, version, name", [param("albums", "v1", "Test Album", id="Albums")]
)
def test_putname_fail(tablename: str, version: str, name: str):
    data = {"AlbumTitle": "More Tests", "ArtistId": 999}
    response = client.put(f"/{tablename}/{version}/name/{name}", json=data)
    print(f"Endpoint = /{tablename}/{version}/name/{name}")
    assert response.status_code == 500


# DELETE Album by Id - PASS
@mark.order(15)
@mark.parametrize(
    "tablename, version, record", [param("albums", "v1", 348, id="Albums")]
)
def test_deleteid_pass(tablename: str, version: str, record: int):
    response = client.delete(f"/{tablename}/{version}/id/{record}")
    print(f"Endpoint = /{tablename}/{version}/id/{record}")
    assert response.status_code == 202


# DELETE Album by Id - FAIL
@mark.order(16)
@mark.parametrize(
    "tablename, version, record", [param("albums", "v1", 348, id="Albums")]
)
def test_deleteid_fail(tablename: str, version: str, record: int):
    response = client.delete(f"/{tablename}/{version}/id/{record}")
    print(f"Endpoint = /{tablename}/{version}/id/{record}")
    assert response.status_code == 404


# DELETE Album by Name - PASS
@mark.order(17)
@mark.parametrize(
    "tablename, version, name", [param("albums", "v1", "Test Album", id="Albums")]
)
def test_deletename_pass(tablename: str, version: str, name: str):
    response = client.delete(f"/{tablename}/{version}/name/{name}")
    print(f"Endpoint = /{tablename}/{version}/name/{name}")
    assert response.status_code == 202


# DELETE Album by Name - FAIL
@mark.order(18)
@mark.parametrize(
    "tablename, version, name", [param("albums", "v1", "Test Album", id="Albums")]
)
def test_deletename_fail(tablename: str, version: str, name: str):
    response = client.delete(f"/{tablename}/{version}/name/{name}")
    print(f"Endpoint = /{tablename}/{version}/name/{name}")
    assert response.status_code == 404
