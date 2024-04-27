from random import randint

from fastapi.testclient import TestClient
from pytest import mark, param

from src.main import app

client = TestClient(app)


# GET All Customers - PASS
@mark.order(1)
@mark.parametrize("tablename, version", [param("customers", "v1", id="Customers")])
def test_getall(tablename: str, version: str, get_count: int):
    num = get_count(tablename)
    response = client.get(f"/{tablename}/{version}")
    print(f"Endpoint = /{tablename}/{version} records {num}")
    assert response.status_code == 200
    assert len(response.json()) == num


# GET RANDOM Customer by Customer Id - PASS
@mark.order(2)
@mark.parametrize("tablename, version", [param("customers", "v1", id="Customers")])
def test_getid_pass(tablename: str, version: str, get_count: int):
    x = randint(1, get_count(tablename))
    response = client.get(f"/{tablename}/{version}/id/{x}")
    print(f"Endpoint = /{tablename}/{version}/id/{x}")
    assert response.status_code == 200
    assert len(response.json()) == 1


# GET Customers by Id - FAIL
@mark.order(3)
@mark.parametrize("tablename, version", [param("customers", "v1", id="Customers")])
def test_getid_fail(tablename: str, version: str, get_count: int):
    num = get_count(tablename) + 1
    response = client.get(f"/{tablename}/{version}/id/{num}")
    print(f"Endpoint = /{tablename}/{version}/id/{num}")
    assert response.status_code == 404


# GET Customers by Name - FAIL
@mark.order(4)
@mark.parametrize(
    "tablename, version, name", [param("customers", "v1", "Not Found", id="Customers")]
)
def test_getname_fail(tablename: str, version: str, name: str):
    response = client.get(f"/{tablename}/{version}/name/{name}")
    print(f"Endpoint = /{tablename}/{version}/name/{name}")
    assert response.status_code == 404


# POST Customer by Name - PASS
@mark.order(5)
@mark.parametrize(
    "tablename, version, name", [param("customers", "v1", "name", id="Customers")]
)
def test_postname_pass1(tablename: str, version: str, name: str):
    data = {
        "Lastname": "Customer 1",
        "Firstname": "Test",
        "Company": "Awesome One",
        "Address": "1, Somewhere",
        "City": "Anywhere",
        "State": "",
        "Country": "",
        "Postalcode": "ABC 123",
        "BillingAddress": "",
        "BillingCity": "",
        "BillingState": "",
        "BillingCountry": "",
        "BillingPostalcode": "",
        "Phone": "",
        "Email": "user@example.com",
        "SupportRepId": 3,
    }
    response = client.post(f"/{tablename}/{version}/name/{name}", json=data)
    print(f"Endpoint = /{tablename}/{version}/name/{name}")
    assert response.status_code == 201


# POST Customer by Name - PASS
@mark.order(6)
@mark.parametrize(
    "tablename, version, name", [param("customers", "v1", "name", id="Customers")]
)
def test_postname_pass2(tablename: str, version: str, name: str):
    data = {
        "Lastname": "Customer 2",
        "Firstname": "Test",
        "Company": "Awesome One",
        "Address": "1, Somewhere",
        "City": "Anywhere",
        "State": "",
        "Country": "",
        "Postalcode": "ABC 123",
        "BillingAddress": "",
        "BillingCity": "",
        "BillingState": "",
        "BillingCountry": "",
        "BillingPostalcode": "",
        "Phone": "",
        "Email": "customer@awesome.com",
        "SupportRepId": 3,
    }
    response = client.post(f"/{tablename}/{version}/name/{name}", json=data)
    print(f"Endpoint = /{tablename}/{version}/name/{name}")
    assert response.status_code == 201


# GET Customers by Name - PASS
@mark.order(7)
@mark.parametrize(
    "tablename, version, name", [param("customers", "v1", "Customer%", id="Customers")]
)
def test_getname_pass(tablename: str, version: str, name: str):
    response = client.get(f"/{tablename}/{version}/name/{name}")
    print(f"Endpoint = /{tablename}/{version}/name/{name}")
    assert response.status_code == 200


# POST Customer by Name - FAIL
@mark.order(8)
@mark.parametrize(
    "tablename, version, name", [param("customers", "v1", "name", id="Customers")]
)
def test_postname_fail(tablename: str, version: str, name: str):
    data = {
        "Lastname": "Customer 1",
        "Firstname": "Test",
        "Company": "Awesome One",
        "Address": "1, Somewhere",
        "City": "Anywhere",
        "State": "",
        "Country": "",
        "Postalcode": "ABC 123",
        "BillingAddress": "",
        "BillingCity": "",
        "BillingState": "",
        "BillingCountry": "",
        "BillingPostalcode": "",
        "Phone": "",
        "Email": "user@example.com",
        "SupportRepId": 3,
    }
    response = client.post(f"/{tablename}/{version}/name/{name}", json=data)
    print(f"Endpoint = /{tablename}/{version}/name/{name}")
    assert response.status_code == 409


# PUT Customer by Id - PASS
@mark.order(9)
@mark.parametrize("tablename, version", [param("customers", "v1", id="Customers")])
def test_putid_pass(tablename: str, version: str, get_count: int):
    num = get_count(tablename)
    data = {
        "Lastname": "Customer 2",
        "Firstname": "Test",
        "Company": "Awesome One",
        "Address": "1, Somewhere",
        "City": "Anywhere",
        "State": "AN",
        "Country": "UK",
        "Postalcode": "ABC 123",
        "BillingAddress": "1, Somewhere",
        "BillingCity": "Anywhere",
        "BillingState": "AN",
        "BillingCountry": "UK",
        "BillingPostalcode": "ABC 123",
        "Phone": "123 654 789",
        "Email": "customer@awesome.com",
        "SupportRepId": 3,
    }
    response = client.put(f"/{tablename}/{version}/id/{num}", json=data)
    print(f"Endpoint = /{tablename}/{version}/id/{num}")
    assert response.status_code == 201


# PUT Customer by Id - FAIL
@mark.order(10)
@mark.parametrize("tablename, version", [param("customers", "v1", id="Customers")])
def test_putid_fail(tablename: str, version: str, get_count: int):
    num = get_count(tablename) + 1
    data = {
        "Lastname": "Customer 1",
        "Firstname": "Test",
        "Company": "Awesome One",
        "Address": "1, Somewhere",
        "City": "Anywhere",
        "State": "AN",
        "Country": "UK",
        "Postalcode": "ABC 123",
        "BillingAddress": "1, Somewhere",
        "BillingCity": "Anywhere",
        "BillingState": "AN",
        "BillingCountry": "UK",
        "BillingPostalcode": "ABC 123",
        "Phone": "+01 123 654 789",
        "Email": "user@example.com",
        "SupportRepId": 3,
    }
    response = client.put(f"/{tablename}/{version}/id/{num}", json=data)
    print(f"Endpoint = /{tablename}/{version}/id/{num}")
    assert response.status_code == 404


# PUT Customer by Name - PASS
@mark.order(11)
@mark.parametrize(
    "tablename, version, name", [param("customers", "v1", "Customer 1", id="Customers")]
)
def test_putname_pass(tablename: str, version: str, name: str):
    data = {
        "Lastname": "Customer 1",
        "Firstname": "Test",
        "Company": "Awesome One",
        "Address": "1, Somewhere",
        "City": "Anywhere",
        "State": "AN",
        "Country": "UK",
        "Postalcode": "ABC 123",
        "BillingAddress": "1, Somewhere",
        "BillingCity": "Anywhere",
        "BillingState": "AN",
        "BillingCountry": "UK",
        "BillingPostalcode": "ABC 123",
        "Phone": "+01 123 654 789",
        "Email": "user@example.com",
        "SupportRepId": 3,
    }
    response = client.put(f"/{tablename}/{version}/name/{name}", json=data)
    print(f"Endpoint = /{tablename}/{version}/name/{name}")
    assert response.status_code == 201


# PUT Customer by Name - FAIL
@mark.order(12)
@mark.parametrize(
    "tablename, version, name", [param("customers", "v1", "Customer 3", id="Customers")]
)
def test_putname_fail(tablename: str, version: str, name: str):
    data = {
        "Lastname": "Customer 1",
        "Firstname": "Test",
        "Company": "Awesome One",
        "Address": "1, Somewhere",
        "City": "Anywhere",
        "State": "AN",
        "Country": "UK",
        "Postalcode": "ABC 123",
        "BillingAddress": "1, Somewhere",
        "BillingCity": "Anywhere",
        "BillingState": "AN",
        "BillingCountry": "UK",
        "BillingPostalcode": "ABC 123",
        "Phone": "+01 123 654 789",
        "Email": "user@example.com",
        "SupportRepId": 9,
    }
    response = client.put(f"/{tablename}/{version}/name/{name}", json=data)
    print(f"Endpoint = /{tablename}/{version}/name/{name}")
    assert response.status_code == 404


# DELETE Customer by Id - PASS
@mark.order(13)
@mark.parametrize("tablename, version", [param("customers", "v1", id="Customers")])
def test_deleteid_pass(tablename: str, version: str, get_count: int):
    num = get_count(tablename)
    response = client.delete(f"/{tablename}/{version}/id/{num}")
    print(f"Endpoint = /{tablename}/{version}/id/{num}")
    assert response.status_code == 202


# DELETE Customer by Id - FAIL
@mark.order(14)
@mark.parametrize("tablename, version", [param("customers", "v1", id="Customers")])
def test_deleteid_fail(tablename: str, version: str, get_count: int):
    num = get_count(tablename) + 1
    response = client.delete(f"/{tablename}/{version}/id/{num}")
    print(f"Endpoint = /{tablename}/{version}/id/{num}")
    assert response.status_code == 404


# DELETE Customer by Name - PASS
@mark.order(15)
@mark.parametrize(
    "tablename, version, name", [param("customers", "v1", "Customer%", id="Customers")]
)
def test_deletename_pass(tablename: str, version: str, name: str):
    response = client.delete(f"/{tablename}/{version}/name/{name}")
    print(f"Endpoint = /{tablename}/{version}/name/{name}")
    assert response.status_code == 202


# DELETE Customer by Name - FAIL
@mark.order(16)
@mark.parametrize(
    "tablename, version, name", [param("customers", "v1", "Customer%", id="Customers")]
)
def test_deletename_fail(tablename: str, version: str, name: str):
    response = client.delete(f"/{tablename}/{version}/name/{name}")
    print(f"Endpoint = /{tablename}/{version}/name/{name}")
    assert response.status_code == 404
