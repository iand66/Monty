from random import randint
from fastapi.testclient import TestClient
from pytest import mark, param
from src.main import app

client = TestClient(app)

# GET All MediaTypes - PASS - Records = 5
@mark.order(1)
@mark.parametrize("tablename, version, record", 
    [param("mediatypes", "v1", 5, id="MediaTypes")])
def test_getall(tablename: str, version: str, record: int):
    response = client.get(f"/{tablename}/{version}")
    print(f"Endpoint = /{tablename}/{version} record count {record}")
    assert response.status_code == 200
    assert len(response.json()) == record

# GET RANDOM MediaType by Id - PASS - One record
@mark.order(2)
@mark.parametrize("tablename, version, record", 
    [param("mediatypes", "v1", 5, id="MediaTypes")])
def test_getid_pass(tablename: str, version: str, record: int):
    x = randint(1, record)
    response = client.get(f"/{tablename}/{version}/id/{x}")
    print(f"Endpoint = /{tablename}/{version}/id/{x}")
    assert response.status_code == 200
    assert len(response.json()) == 1

# GET MediaTypes by Id - FAIL - Detail not found
@mark.order(3)
@mark.parametrize("tablename, version, record", 
    [param("mediatypes", "v1", 999, id="MediaTypes")])
def test_getid_fail(tablename: str, version: str, record: int):
    response = client.get(f"/{tablename}/{version}/id/{record}")
    print(f"Endpoint = /{tablename}/{version}/id/{record}")
    assert response.status_code == 404

# GET MediaTypes by Name - PASS - Single record
@mark.order(6)
@mark.parametrize("tablename, version, name", 
    [param("mediatypes", "v1", "Test MediaType 1", id="MediaTypes")])
def test_getname_pass(tablename: str, version: str, name: str):
    response = client.get(f"/{tablename}/{version}/name/{name}")
    print(f"Endpoint = /{tablename}/{version}/name/{name}")
    assert response.status_code == 200

# GET MediaTypes by Name - FAIL - Detail not found
@mark.order(7)
@mark.parametrize("tablename, version, name", 
    [param("mediatypes", "v1", "Not Found", id="MediaTypes")])
def test_getname_fail(tablename: str, version: str, name: str):
    response = client.get(f"/{tablename}/{version}/name/{name}")
    print(f"Endpoint = /{tablename}/{version}/name/{name}")
    assert response.status_code == 404

# POST MediaType by Name - PASS - New record
@mark.order(4)
@mark.parametrize("tablename, version, name", 
    [param("mediatypes", "v1", "name", id="MediaTypes")])
def test_postname_pass1(tablename: str, version: str, name: str):
    data = {"MediaTypeName":"Test MediaType 1"}
    response = client.post(f"/{tablename}/{version}/name/{name}", json=data)
    print(f"Endpoint = /{tablename}/{version}/name/{name}")
    assert response.status_code == 201

# POST MediaType by Name - PASS - New record
@mark.order(5)
@mark.parametrize("tablename, version, name", 
    [param("mediatypes", "v1", "name", id="MediaTypes")])
def test_postname_pass2(tablename: str, version: str, name: str):
    data = {"MediaTypeName":"Test MediaType 2"}
    response = client.post(f"/{tablename}/{version}/name/{name}", json=data)
    print(f"Endpoint = /{tablename}/{version}/name/{name}")
    assert response.status_code == 201

# POST MediaType by Name - FAIL - Duplicate record
@mark.order(8)
@mark.parametrize("tablename, version, name", 
    [param("mediatypes", "v1", "name", id="MediaTypes")])
def test_postname_fail(tablename: str, version: str, name: str):
    data = {"MediaTypeName":"Test MediaType 2"}
    response = client.post(f"/{tablename}/{version}/name/{name}", json=data)
    print(f"Endpoint = /{tablename}/{version}/name/{name}")
    assert response.status_code == 409

# PUT MediaType by Name - PASS - MediaTypeName
@mark.order(9)
@mark.parametrize("tablename, version, record", 
    [param("mediatypes", "v1", 6, id="MediaTypes")])
def test_putname_pass(tablename: str, version: str, record: int):
    data = {"MediaTypeName":"Test MediaType Renamed"}
    response = client.put(f"/{tablename}/{version}/id/{record}", json=data)
    print(f"Endpoint = /{tablename}/{version}/name/{record}")
    assert response.status_code == 201
    
# PUT MediaType by Name - FAIL - Unknown Id
@mark.order(10)
@mark.parametrize("tablename, version, record", 
    [param("mediatypes", "v1", 999, id="MediaTypes")])
def test_putname_fail(tablename: str, version: str, record: int):
    data = {"MediaTypeName":"Does Not Matter"}
    response = client.put(f"/{tablename}/{version}/id/{record}", json=data)
    print(f"Endpoint = /{tablename}/{version}/id/{record}")
    assert response.status_code == 404
    
# DELETE MediaType by Id - PASS
@mark.order(11)
@mark.parametrize("tablename, version, record", 
    [param("mediatypes", "v1" , 6, id="MediaTypes")])
def test_deleteid_pass(tablename: str, version: str, record: int):
    response = client.delete(f"/{tablename}/{version}/id/{record}")
    print(f"Endpoint = /{tablename}/{version}/id/{record}")
    assert response.status_code == 202

# DELETE MediaType by Id - FAIL - Unknown Id
@mark.order(12)
@mark.parametrize("tablename, version, record", 
    [param("mediatypes", "v1", 6, id="MediaTypes")])
def test_deleteid_fail(tablename: str, version: str, record: int):
    response = client.delete(f"/{tablename}/{version}/id/{record}")
    print(f"Endpoint = /{tablename}/{version}/id/{record}")
    assert response.status_code == 404

# DELETE MediaType by Name - PASS
@mark.order(13)
@mark.parametrize("tablename, version, name", 
    [param("mediatypes", "v1", "Test MediaType%", id="MediaTypes")])
def test_deletename_pass(tablename: str, version: str, name: str):
    response = client.delete(f"/{tablename}/{version}/name/{name}")
    print(f"Endpoint = /{tablename}/{version}/name/{name}")
    assert response.status_code == 202

# DELETE MediaType by Name - FAIL - Not Found
@mark.order(14)
@mark.parametrize("tablename, version, name", 
    [param("mediatypes", "v1", "Test MediaType", id="MediaTypes")])
def test_deletename_fail(tablename: str, version: str, name: str):
    response = client.delete(f"/{tablename}/{version}/name/{name}")
    print(f"Endpoint = /{tablename}/{version}/name/{name}")
    assert response.status_code == 404