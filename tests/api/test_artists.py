from random import randint
from fastapi.testclient import TestClient
from pytest import mark, param
from src.main import app

client = TestClient(app)

# GET All Artists - PASS - Records = 275
@mark.order(1)
@mark.parametrize("tablename, version, record", 
    [param("artists", "v1", 275, id="Artists")])
def test_getall(tablename: str, version: str, record: int):
    response = client.get(f"/{tablename}/{version}")
    print(f"Endpoint = /{tablename}/{version} record count {record}")
    assert response.status_code == 200
    assert len(response.json()) == record

# GET RANDOM Artist by Artist Id - PASS - One record
@mark.order(2)
@mark.parametrize("tablename, version, record", 
    [param("artists", "v1", 275, id="Artists")])
def test_getid_pass(tablename: str, version: str, record: int):
    x = randint(1, record)
    response = client.get(f"/{tablename}/{version}/id/{x}")
    print(f"Endpoint = /{tablename}/{version}/id/{x}")
    assert response.status_code == 200
    assert len(response.json()) == 1

# GET Artists by Id - FAIL - Detail not found
@mark.order(3)
@mark.parametrize("tablename, version, record", 
    [param("artists", "v1", 999, id="Artists")])
def test_getid_fail(tablename: str, version: str, record: int):
    response = client.get(f"/{tablename}/{version}/id/{record}")
    print(f"Endpoint = /{tablename}/{version}/id/{record}")
    assert response.status_code == 404

# GET Artists by Name - PASS - Single record
@mark.order(6)
@mark.parametrize("tablename, version, name", 
    [param("artists", "v1", "Test Artist 1", id="Artists")])
def test_getname_pass(tablename: str, version: str, name: str):
    response = client.get(f"/{tablename}/{version}/name/{name}")
    print(f"Endpoint = /{tablename}/{version}/name/{name}")
    assert response.status_code == 200

# GET Artists by Name - FAIL - Detail not found
@mark.order(7)
@mark.parametrize("tablename, version, name", 
    [param("artists", "v1", "Not Found", id="Artists")])
def test_getname_fail(tablename: str, version: str, name: str):
    response = client.get(f"/{tablename}/{version}/name/{name}")
    print(f"Endpoint = /{tablename}/{version}/name/{name}")
    assert response.status_code == 404

# POST Artist by Name - PASS - New record
@mark.order(4)
@mark.parametrize("tablename, version, name", 
    [param("artists", "v1", "name", id="Artists")])
def test_postname_pass1(tablename: str, version: str, name: str):
    data = {"ArtistName":"Test Artist 1"}
    response = client.post(f"/{tablename}/{version}/name/{name}", json=data)
    print(f"Endpoint = /{tablename}/{version}/name/{name}")
    assert response.status_code == 201

# POST Artist by Name - PASS - New record
@mark.order(5)
@mark.parametrize("tablename, version, name", 
    [param("artists", "v1", "name", id="Artists")])
def test_postname_pass2(tablename: str, version: str, name: str):
    data = {"ArtistName":"Test Artist 2"}
    response = client.post(f"/{tablename}/{version}/name/{name}", json=data)
    print(f"Endpoint = /{tablename}/{version}/name/{name}")
    assert response.status_code == 201

# POST Artist by Name - FAIL - Duplicate record
@mark.order(8)
@mark.parametrize("tablename, version, name", 
    [param("artists", "v1", "name", id="Artists")])
def test_postname_fail(tablename: str, version: str, name: str):
    data = {"ArtistName":"Test Artist 1"}
    response = client.post(f"/{tablename}/{version}/name/{name}", json=data)
    print(f"Endpoint = /{tablename}/{version}/name/{name}")
    assert response.status_code == 409

# PUT Artist by Name - PASS - ArtistName
@mark.order(9)
@mark.parametrize("tablename, version, record", 
    [param("artists", "v1", 276, id="Artists")])
def test_putname_pass(tablename: str, version: str, record: int):
    data = {"ArtistName":"Another Test"}
    response = client.put(f"/{tablename}/{version}/id/{record}", json=data)
    print(f"Endpoint = /{tablename}/{version}/name/{record}")
    assert response.status_code == 201
    
# PUT Artist by Name - FAIL - Unknown Id
@mark.order(10)
@mark.parametrize("tablename, version, record", 
    [param("artists", "v1", 999, id="Artists")])
def test_putname_fail(tablename: str, version: str, record: int):
    data = {"ArtistName":"Does Not Matter"}
    response = client.put(f"/{tablename}/{version}/id/{record}", json=data)
    print(f"Endpoint = /{tablename}/{version}/id/{record}")
    assert response.status_code == 404
    
# DELETE Artist by Id - PASS
@mark.order(11)
@mark.parametrize("tablename, version, record", 
    [param("artists", "v1" , 276, id="Artists")])
def test_deleteid_pass(tablename: str, version: str, record: int):
    response = client.delete(f"/{tablename}/{version}/id/{record}")
    print(f"Endpoint = /{tablename}/{version}/id/{record}")
    assert response.status_code == 202

# DELETE Artist by Id - FAIL - Unknown Id
@mark.order(12)
@mark.parametrize("tablename, version, record", 
    [param("artists", "v1", 276, id="Artists")])
def test_deleteid_fail(tablename: str, version: str, record: int):
    response = client.delete(f"/{tablename}/{version}/id/{record}")
    print(f"Endpoint = /{tablename}/{version}/id/{record}")
    assert response.status_code == 404

# DELETE Artist by Name - PASS
@mark.order(13)
@mark.parametrize("tablename, version, name", 
    [param("artists", "v1", "Test Artist%", id="Artists")])
def test_deletename_pass(tablename: str, version: str, name: str):
    response = client.delete(f"/{tablename}/{version}/name/{name}")
    print(f"Endpoint = /{tablename}/{version}/name/{name}")
    assert response.status_code == 202

# DELETE Artist by Name - FAIL - Not Found
@mark.order(14)
@mark.parametrize("tablename, version, name", 
    [param("artists", "v1", "Test Artist", id="Artists")])
def test_deletename_fail(tablename: str, version: str, name: str):
    response = client.delete(f"/{tablename}/{version}/name/{name}")
    print(f"Endpoint = /{tablename}/{version}/name/{name}")
    assert response.status_code == 404