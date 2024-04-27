from random import randint

from fastapi.testclient import TestClient
from pytest import mark, param

from src.main import app

client = TestClient(app)


# GET All Playlists - PASS
@mark.order(1)
@mark.parametrize("tablename, version", [param("playlists", "v1", id="Playlists")])
def test_getall(tablename: str, version: str, get_count: int):
    num = get_count(tablename)
    response = client.get(f"/{tablename}/{version}")
    print(f"Endpoint = /{tablename}/{num} records {num}")
    assert response.status_code == 200
    assert len(response.json()) == num


# GET RANDOM Playlist by Playlist Id - PASS
@mark.order(2)
@mark.parametrize("tablename, version", [param("playlists", "v1", id="Playlists")])
def test_getid_pass(tablename: str, version: str, get_count: int):
    x = randint(1, get_count(tablename))
    response = client.get(f"/{tablename}/{version}/id/{x}")
    print(f"Endpoint = /{tablename}/{version}/id/{x}")
    assert response.status_code == 200
    assert len(response.json()) == 1


# GET Playlists by Id - FAIL
@mark.order(3)
@mark.parametrize("tablename, version", [param("playlists", "v1", id="Playlists")])
def test_getid_fail(tablename: str, version: str, get_count: int):
    num = get_count(tablename) + 1
    response = client.get(f"/{tablename}/{version}/id/{num}")
    print(f"Endpoint = /{tablename}/{version}/id/{num}")
    assert response.status_code == 404


# GET Playlists by Name - FAIL
@mark.order(4)
@mark.parametrize(
    "tablename, version, name", [param("playlists", "v1", "Not Found", id="Playlists")]
)
def test_getname_fail(tablename: str, version: str, name: str):
    response = client.get(f"/{tablename}/{version}/name/{name}")
    print(f"Endpoint = /{tablename}/{version}/name/{name}")
    assert response.status_code == 404


# POST Playlist by Name - PASS
@mark.order(5)
@mark.parametrize(
    "tablename, version, name", [param("playlists", "v1", "name", id="Playlists")]
)
def test_postname_pass1(tablename: str, version: str, name: str):
    data = {"PlaylistName": "Test Playlist 1"}
    response = client.post(f"/{tablename}/{version}/name/{name}", json=data)
    print(f"Endpoint = /{tablename}/{version}/name/{name}")
    assert response.status_code == 201


# POST Playlist by Name - PASS
@mark.order(6)
@mark.parametrize(
    "tablename, version, name", [param("playlists", "v1", "name", id="Playlists")]
)
def test_postname_pass2(tablename: str, version: str, name: str):
    data = {"PlaylistName": "Test Playlist 2"}
    response = client.post(f"/{tablename}/{version}/name/{name}", json=data)
    print(f"Endpoint = /{tablename}/{version}/name/{name}")
    assert response.status_code == 201


# GET Playlists by Name - PASS
@mark.order(7)
@mark.parametrize(
    "tablename, version, name",
    [param("playlists", "v1", "Test Playlist%", id="Playlists")],
)
def test_getname_pass(tablename: str, version: str, name: str):
    response = client.get(f"/{tablename}/{version}/name/{name}")
    print(f"Endpoint = /{tablename}/{version}/name/{name}")
    assert response.status_code == 200


# POST Playlist by Name - FAIL
@mark.order(8)
@mark.parametrize(
    "tablename, version, name", [param("playlists", "v1", "name", id="Playlists")]
)
def test_postname_fail(tablename: str, version: str, name: str):
    data = {"PlaylistName": "Test Playlist 1"}
    response = client.post(f"/{tablename}/{version}/name/{name}", json=data)
    print(f"Endpoint = /{tablename}/{version}/name/{name}")
    assert response.status_code == 409


# PUT Playlist by Id - PASS
@mark.order(9)
@mark.parametrize("tablename, version", [param("playlists", "v1", id="Playlists")])
def test_putid_pass(tablename: str, version: str, get_count: int):
    num = get_count(tablename)
    data = {"PlaylistName": "Test Playlist 3"}
    response = client.put(f"/{tablename}/{version}/id/{num}", json=data)
    print(f"Endpoint = /{tablename}/{version}/id/{num}")
    assert response.status_code == 201


# PUT Playlist by Id - FAIL
@mark.order(10)
@mark.parametrize("tablename, version", [param("playlists", "v1", id="Playlists")])
def test_putid_fail(tablename: str, version: str, get_count: int):
    num = get_count(tablename) + 1
    data = {"PlaylistName": "Test Playlist 1"}
    response = client.put(f"/{tablename}/{version}/id/{num}", json=data)
    print(f"Endpoint = /{tablename}/{version}/id/{num}")
    assert response.status_code == 404


# PUT Playlist by Name - PASS
@mark.order(11)
@mark.parametrize(
    "tablename, version, name",
    [param("playlists", "v1", "Test Playlist 3", id="Playlists")],
)
def test_putname_pass(tablename: str, version: str, name: str):
    data = {"PlaylistName": "Test Playlist 2"}
    response = client.put(f"/{tablename}/{version}/name/{name}", json=data)
    print(f"Endpoint = /{tablename}/{version}/name/{name}")
    assert response.status_code == 201


# PUT Playlist by Name - FAIL
@mark.order(12)
@mark.parametrize(
    "tablename, version, name",
    [param("playlists", "v1", "Test Playlist 3", id="Playlists")],
)
def test_putname_fail(tablename: str, version: str, name: str):
    data = {"PlaylistName": "Test Playlist 3"}
    response = client.put(f"/{tablename}/{version}/name/{name}", json=data)
    print(f"Endpoint = /{tablename}/{version}/name/{name}")
    assert response.status_code == 404


# DELETE Playlist by Id - PASS
@mark.order(13)
@mark.parametrize("tablename, version", [param("playlists", "v1", id="Playlists")])
def test_deleteid_pass(tablename: str, version: str, get_count: int):
    num = get_count(tablename)
    response = client.delete(f"/{tablename}/{version}/id/{num}")
    print(f"Endpoint = /{tablename}/{version}/id/{num}")
    assert response.status_code == 202


# DELETE Playlist by Id - FAIL
@mark.order(14)
@mark.parametrize("tablename, version", [param("playlists", "v1", id="Playlists")])
def test_deleteid_fail(tablename: str, version: str, get_count: int):
    num = get_count(tablename) + 1
    response = client.delete(f"/{tablename}/{version}/id/{num}")
    print(f"Endpoint = /{tablename}/{version}/id/{num}")
    assert response.status_code == 404


# DELETE Playlist by Name - PASS
@mark.order(15)
@mark.parametrize(
    "tablename, version, name",
    [param("playlists", "v1", "Test Playlist%", id="Playlists")],
)
def test_deletename_pass(tablename: str, version: str, name: str):
    response = client.delete(f"/{tablename}/{version}/name/{name}")
    print(f"Endpoint = /{tablename}/{version}/name/{name}")
    assert response.status_code == 202


# DELETE Playlist by Name - FAIL
@mark.order(16)
@mark.parametrize(
    "tablename, version, name",
    [param("playlists", "v1", "Test Playlist%", id="Playlists")],
)
def test_deletename_fail(tablename: str, version: str, name: str):
    response = client.delete(f"/{tablename}/{version}/name/{name}")
    print(f"Endpoint = /{tablename}/{version}/name/{name}")
    assert response.status_code == 404
