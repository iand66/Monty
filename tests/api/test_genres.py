from random import randint
from fastapi.testclient import TestClient
from pytest import mark, param
from src.main import app

client = TestClient(app)

# GET All Genres - PASS - Records = 25
@mark.order(1)
@mark.parametrize("tablename, version, record", 
    [param("genres", "v1", 25, id="Genres")])
def test_getall(tablename: str, version: str, record: int):
    response = client.get(f"/{tablename}/{version}")
    print(f"Endpoint = /{tablename}/{version} record count {record}")
    assert response.status_code == 200
    assert len(response.json()) == record

# GET RANDOM Genre by Genre Id - PASS - One record
@mark.order(2)
@mark.parametrize("tablename, version, record", 
    [param("genres", "v1", 25, id="Genres")])
def test_getid_pass(tablename: str, version: str, record: int):
    x = randint(1, record)
    response = client.get(f"/{tablename}/{version}/id/{x}")
    print(f"Endpoint = /{tablename}/{version}/id/{x}")
    assert response.status_code == 200
    assert len(response.json()) == 1

# GET Genres by Id - FAIL - Detail not found
@mark.order(3)
@mark.parametrize("tablename, version, record", 
    [param("genres", "v1", 999, id="Genres")])
def test_getid_fail(tablename: str, version: str, record: int):
    response = client.get(f"/{tablename}/{version}/id/{record}")
    print(f"Endpoint = /{tablename}/{version}/id/{record}")
    assert response.status_code == 404

# GET Genres by Name - PASS - Single record
@mark.order(6)
@mark.parametrize("tablename, version, name", 
    [param("genres", "v1", "Test Genre 1", id="Genres")])
def test_getname_pass(tablename: str, version: str, name: str):
    response = client.get(f"/{tablename}/{version}/name/{name}")
    print(f"Endpoint = /{tablename}/{version}/name/{name}")
    assert response.status_code == 200

# GET Genres by Name - FAIL - Detail not found
@mark.order(7)
@mark.parametrize("tablename, version, name", 
    [param("genres", "v1", "Not Found", id="Genres")])
def test_getname_fail(tablename: str, version: str, name: str):
    response = client.get(f"/{tablename}/{version}/name/{name}")
    print(f"Endpoint = /{tablename}/{version}/name/{name}")
    assert response.status_code == 404

# POST Genre by Name - PASS - New record
@mark.order(4)
@mark.parametrize("tablename, version, name", 
    [param("genres", "v1", "name", id="Genres")])
def test_postname_pass1(tablename: str, version: str, name: str):
    data = {"GenreName":"Test Genre 1"}
    response = client.post(f"/{tablename}/{version}/name/{name}", json=data)
    print(f"Endpoint = /{tablename}/{version}/name/{name}")
    assert response.status_code == 201

# POST Genre by Name - PASS - New record
@mark.order(5)
@mark.parametrize("tablename, version, name", 
    [param("genres", "v1", "name", id="Genres")])
def test_postname_pass2(tablename: str, version: str, name: str):
    data = {"GenreName":"Test Genre 2"}
    response = client.post(f"/{tablename}/{version}/name/{name}", json=data)
    print(f"Endpoint = /{tablename}/{version}/name/{name}")
    assert response.status_code == 201

# POST Genre by Name - FAIL - Duplicate record
@mark.order(8)
@mark.parametrize("tablename, version, name", 
    [param("genres", "v1", "name", id="Genres")])
def test_postname_fail(tablename: str, version: str, name: str):
    data = {"GenreName":"Test Genre 2"}
    response = client.post(f"/{tablename}/{version}/name/{name}", json=data)
    print(f"Endpoint = /{tablename}/{version}/name/{name}")
    assert response.status_code == 409

# PUT Genre by Name - PASS - GenreName
@mark.order(9)
@mark.parametrize("tablename, version, record", 
    [param("genres", "v1", 26, id="Genres")])
def test_putname_pass(tablename: str, version: str, record: int):
    data = {"GenreName":"Test Genre Renamed"}
    response = client.put(f"/{tablename}/{version}/id/{record}", json=data)
    print(f"Endpoint = /{tablename}/{version}/name/{record}")
    assert response.status_code == 201
    
# PUT Genre by Name - FAIL - Unknown Id
@mark.order(10)
@mark.parametrize("tablename, version, record", 
    [param("genres", "v1", 999, id="Genres")])
def test_putname_fail(tablename: str, version: str, record: int):
    data = {"GenreName":"Does Not Matter"}
    response = client.put(f"/{tablename}/{version}/id/{record}", json=data)
    print(f"Endpoint = /{tablename}/{version}/id/{record}")
    assert response.status_code == 404
    
# DELETE Genre by Id - PASS
@mark.order(11)
@mark.parametrize("tablename, version, record", 
    [param("genres", "v1" , 26, id="Genres")])
def test_deleteid_pass(tablename: str, version: str, record: int):
    response = client.delete(f"/{tablename}/{version}/id/{record}")
    print(f"Endpoint = /{tablename}/{version}/id/{record}")
    assert response.status_code == 202

# DELETE Genre by Id - FAIL - Unknown Id
@mark.order(12)
@mark.parametrize("tablename, version, record", 
    [param("genres", "v1", 26, id="Genres")])
def test_deleteid_fail(tablename: str, version: str, record: int):
    response = client.delete(f"/{tablename}/{version}/id/{record}")
    print(f"Endpoint = /{tablename}/{version}/id/{record}")
    assert response.status_code == 404

# DELETE Genre by Name - PASS
@mark.order(13)
@mark.parametrize("tablename, version, name", 
    [param("genres", "v1", "Test Genre%", id="Genres")])
def test_deletename_pass(tablename: str, version: str, name: str):
    response = client.delete(f"/{tablename}/{version}/name/{name}")
    print(f"Endpoint = /{tablename}/{version}/name/{name}")
    assert response.status_code == 202

# DELETE Genre by Name - FAIL - Not Found
@mark.order(14)
@mark.parametrize("tablename, version, name", 
    [param("genres", "v1", "Test Genre", id="Genres")])
def test_deletename_fail(tablename: str, version: str, name: str):
    response = client.delete(f"/{tablename}/{version}/name/{name}")
    print(f"Endpoint = /{tablename}/{version}/name/{name}")
    assert response.status_code == 404