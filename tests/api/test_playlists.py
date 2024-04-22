from random import randint

from sqlalchemy import text
from fastapi.testclient import TestClient
from pytest import mark, param, fixture

from src.main import app

client = TestClient(app)


@fixture
def num_playlists(get_db):
    result = get_db.execute(text("SELECT COUNT(*) FROM playlists"))
    count = result.fetchone()[0]
    return count


# GET All Playlists - PASS
@mark.order(1)
@mark.parametrize("tablename, version", [param("playlists", "v1", id="Playlists")])
def test_getall(tablename: str, version: str, num_playlists: int):
    response = client.get(f"/{tablename}/{version}")
    print(f"Endpoint = /{tablename}/{num_playlists} records {num_playlists}")
    assert response.status_code == 200
    assert len(response.json()) == num_playlists


# GET RANDOM Playlist by Playlist Id - PASS
@mark.order(2)
@mark.parametrize("tablename, version", [param("playlists", "v1", id="Playlists")])
def test_getid_pass(tablename: str, version: str, num_playlists: int):
    x = randint(1, num_playlists)
    response = client.get(f"/{tablename}/{version}/id/{x}")
    print(f"Endpoint = /{tablename}/{version}/id/{x}")
    assert response.status_code == 200
    assert len(response.json()) == 1


# GET Playlists by Id - FAIL
@mark.order(3)
@mark.parametrize("tablename, version", [param("playlists", "v1", id="Playlists")])
def test_getid_fail(tablename: str, version: str, num_playlists: int):
    num_playlists = num_playlists + 1
    response = client.get(f"/{tablename}/{version}/id/{num_playlists}")
    print(f"Endpoint = /{tablename}/{version}/id/{num_playlists}")
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
def test_putid_pass(tablename: str, version: str, num_playlists: int):
    data = {"PlaylistName": "Test Playlist 3"}
    response = client.put(f"/{tablename}/{version}/id/{num_playlists}", json=data)
    print(f"Endpoint = /{tablename}/{version}/id/{num_playlists}")
    assert response.status_code == 201


# PUT Playlist by Id - FAIL
@mark.order(10)
@mark.parametrize("tablename, version", [param("playlists", "v1", id="Playlists")])
def test_putid_fail(tablename: str, version: str, num_playlists: int):
    num_playlists = num_playlists + 1
    data = {"PlaylistName": "Test Playlist 1"}
    response = client.put(f"/{tablename}/{version}/id/{num_playlists}", json=data)
    print(f"Endpoint = /{tablename}/{version}/id/{num_playlists}")
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
    data = {"PlaylistName": "Test Playlist 1"}
    response = client.put(f"/{tablename}/{version}/name/{name}", json=data)
    print(f"Endpoint = /{tablename}/{version}/name/{name}")
    assert response.status_code == 404


# DELETE Playlist by Id - PASS
@mark.order(13)
@mark.parametrize("tablename, version", [param("playlists", "v1", id="Playlists")])
def test_deleteid_pass(tablename: str, version: str, num_playlists: int):
    response = client.delete(f"/{tablename}/{version}/id/{num_playlists}")
    print(f"Endpoint = /{tablename}/{version}/id/{num_playlists}")
    assert response.status_code == 202


# DELETE Playlist by Id - FAIL
@mark.order(14)
@mark.parametrize("tablename, version", [param("playlists", "v1", id="Playlists")])
def test_deleteid_fail(tablename: str, version: str, num_playlists: int):
    num_playlists = num_playlists + 1
    response = client.delete(f"/{tablename}/{version}/id/{num_playlists}")
    print(f"Endpoint = /{tablename}/{version}/id/{num_playlists}")
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
