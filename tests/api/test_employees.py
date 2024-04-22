from random import randint

from sqlalchemy import text
from fastapi.testclient import TestClient
from pytest import mark, param, fixture

from src.main import app

client = TestClient(app)


@fixture
def num_employees(get_db):
    result = get_db.execute(text("SELECT COUNT(*) FROM employees"))
    count = result.fetchone()[0]
    return count


# GET All Employees - PASS
@mark.order(1)
@mark.parametrize("tablename, version", [param("employees", "v1", id="Employees")])
def test_getall(tablename: str, version: str, num_employees: int):
    response = client.get(f"/{tablename}/{version}")
    print(f"Endpoint = /{tablename}/{version} records {num_employees}")
    assert response.status_code == 200
    assert len(response.json()) == num_employees


# GET RANDOM Employee by Employee Id - PASS
@mark.order(2)
@mark.parametrize("tablename, version", [param("employees", "v1", id="Employees")])
def test_getid_pass(tablename: str, version: str, num_employees: int):
    x = randint(1, num_employees)
    response = client.get(f"/{tablename}/{version}/id/{x}")
    print(f"Endpoint = /{tablename}/{version}/id/{x}")
    assert response.status_code == 200
    assert len(response.json()) == 1


# GET Employees by Id - FAIL
@mark.order(3)
@mark.parametrize("tablename, version", [param("employees", "v1", id="Employees")])
def test_getid_fail(tablename: str, version: str, num_employees: int):
    num_employees = num_employees + 1
    response = client.get(f"/{tablename}/{version}/id/{num_employees}")
    print(f"Endpoint = /{tablename}/{version}/id/{num_employees}")
    assert response.status_code == 404


# GET Employees by Name - FAIL
@mark.order(4)
@mark.parametrize(
    "tablename, version, name", [param("employees", "v1", "Not Found", id="Employees")]
)
def test_getname_fail(tablename: str, version: str, name: str):
    response = client.get(f"/{tablename}/{version}/name/{name}")
    print(f"Endpoint = /{tablename}/{version}/name/{name}")
    assert response.status_code == 404


# POST Employee by Name - PASS
@mark.order(5)
@mark.parametrize(
    "tablename, version, name", [param("employees", "v1", "name", id="Employees")]
)
def test_postname_pass1(tablename: str, version: str, name: str):
    data = {
        "Lastname": "Employee 1",
        "Firstname": "Temp",
        "Title": "Temp Employee",
        "ReportsTo": 1,
        "Birthdate": None,
        "Hiredate": None,
        "Address": "",
        "City": "",
        "State": "",
        "Country": "",
        "Postalcode": "",
        "Phone": "",
        "Email": "temp1@chinookcorp.com",
    }
    response = client.post(f"/{tablename}/{version}/name/{name}", json=data)
    print(f"Endpoint = /{tablename}/{version}/name/{name}")
    assert response.status_code == 201


# POST Employee by Name - PASS
@mark.order(6)
@mark.parametrize(
    "tablename, version, name", [param("employees", "v1", "name", id="Employees")]
)
def test_postname_pass2(tablename: str, version: str, name: str):
    data = {
        "Lastname": "Employee 2",
        "Firstname": "Temp",
        "Title": "Temp Employee",
        "ReportsTo": 1,
        "Birthdate": None,
        "Hiredate": None,
        "Address": "",
        "City": "",
        "State": "",
        "Country": "",
        "Postalcode": "",
        "Phone": "",
        "Email": "temp2@chinookcorp.com",
    }
    response = client.post(f"/{tablename}/{version}/name/{name}", json=data)
    print(f"Endpoint = /{tablename}/{version}/name/{name}")
    assert response.status_code == 201


# GET Employees by Name - PASS
@mark.order(7)
@mark.parametrize(
    "tablename, version, name", [param("employees", "v1", "Employee%", id="Employees")]
)
def test_getname_pass(tablename: str, version: str, name: str):
    response = client.get(f"/{tablename}/{version}/name/{name}")
    print(f"Endpoint = /{tablename}/{version}/name/{name}")
    assert response.status_code == 200


# POST Employee by Name - FAIL
@mark.order(8)
@mark.parametrize(
    "tablename, version, name", [param("employees", "v1", "name", id="Employees")]
)
def test_postname_fail(tablename: str, version: str, name: str):
    data = {
        "Lastname": "Employee 1",
        "Firstname": "Temp",
        "Title": "Temp Employee",
        "ReportsTo": 1,
        "Birthdate": None,
        "Hiredate": None,
        "Address": "",
        "City": "",
        "State": "",
        "Country": "",
        "Postalcode": "",
        "Phone": "",
        "Email": "temp1@chinookcorp.com",
    }
    response = client.post(f"/{tablename}/{version}/name/{name}", json=data)
    print(f"Endpoint = /{tablename}/{version}/name/{name}")
    assert response.status_code == 409


# PUT Employee by Id - PASS
@mark.order(9)
@mark.parametrize("tablename, version", [param("employees", "v1", id="Employees")])
def test_putid_pass(tablename: str, version: str, num_employees: int):
    num_employees = num_employees - 1
    data = {
        "Lastname": "Employee 1",
        "Firstname": "Temp",
        "Title": "Temp Employee",
        "ReportsTo": 1,
        "Birthdate": None,
        "Hiredate": None,
        "Address": "11120 Jasper Ave NW",
        "City": "Edmonton",
        "State": "AB",
        "Country": "Canada",
        "Postalcode": "T5K 2N1",
        "Phone": "+1 (780) 428-9482",
        "Email": "temp1@chinookcorp.com",
    }
    response = client.put(f"/{tablename}/{version}/id/{num_employees}", json=data)
    print(f"Endpoint = /{tablename}/{version}/id/{num_employees}")
    assert response.status_code == 201


# PUT Employee by Id - FAIL
@mark.order(10)
@mark.parametrize("tablename, version", [param("employees", "v1", id="Employees")])
def test_putid_fail(tablename: str, version: str, num_employees: int):
    num_employees = num_employees + 1
    data = {
        "Lastname": "Employee 1",
        "Firstname": "Temp",
        "Title": "Temp Employee",
        "ReportsTo": 1,
        "Birthdate": None,
        "Hiredate": None,
        "Address": "11120 Jasper Ave NW",
        "City": "Edmonton",
        "State": "AB",
        "Country": "Canada",
        "Postalcode": "T5K 2N1",
        "Phone": "+1 (780) 428-9482",
        "Email": "temp1@chinookcorp.com",
    }
    response = client.put(f"/{tablename}/{version}/id/{num_employees}", json=data)
    print(f"Endpoint = /{tablename}/{version}/id/{num_employees}")
    assert response.status_code == 404


# PUT Employee by Name - PASS
@mark.order(11)
@mark.parametrize(
    "tablename, version, name", [param("employees", "v1", "Employee 1", id="Employees")]
)
def test_putname_pass(tablename: str, version: str, name: str):
    data = {
        "Lastname": "Employee 1",
        "Firstname": "Temp",
        "Title": "Temp Employee",
        "ReportsTo": 6,
        "Birthdate": None,
        "Hiredate": None,
        "Address": "5827 Bowness Road NW",
        "City": "Calgary",
        "State": "AB",
        "Country": "Canada",
        "Postalcode": "T3B 0C5",
        "Phone": "+1 (403) 246-9887",
        "Email": "temp1@chinookcorp.com",
    }
    response = client.put(f"/{tablename}/{version}/name/{name}", json=data)
    print(f"Endpoint = /{tablename}/{version}/name/{name}")
    assert response.status_code == 201


# PUT Employee by Name - FAIL
@mark.order(12)
@mark.parametrize(
    "tablename, version, name", [param("employees", "v1", "Employee 3", id="Employees")]
)
def test_putname_fail(tablename: str, version: str, name: str):
    data = {
        "Lastname": "Employee 1",
        "Firstname": "Temp",
        "Title": "Temp Employee",
        "ReportsTo": 6,
        "Birthdate": None,
        "Hiredate": None,
        "Address": "5827 Bowness Road NW",
        "City": "Calgary",
        "State": "AB",
        "Country": "Canada",
        "Postalcode": "T3B 0C5",
        "Phone": "+1 (403) 246-9887",
        "Email": "temp1@chinookcorp.com",
    }
    response = client.put(f"/{tablename}/{version}/name/{name}", json=data)
    print(f"Endpoint = /{tablename}/{version}/name/{name}")
    assert response.status_code == 404


# DELETE Employee by Id - PASS
@mark.order(13)
@mark.parametrize("tablename, version", [param("employees", "v1", id="Employees")])
def test_deleteid_pass(tablename: str, version: str, num_employees: int):
    num_employees = num_employees - 1
    response = client.delete(f"/{tablename}/{version}/id/{num_employees}")
    print(f"Endpoint = /{tablename}/{version}/id/{num_employees}")
    assert response.status_code == 202


# DELETE Employee by Id - FAIL
@mark.order(14)
@mark.parametrize("tablename, version", [param("employees", "v1", id="Employees")])
def test_deleteid_fail(tablename: str, version: str, num_employees: int):
    num_employees = num_employees + 2
    response = client.delete(f"/{tablename}/{version}/id/{num_employees}")
    print(f"Endpoint = /{tablename}/{version}/id/{num_employees}")
    assert response.status_code == 404


# DELETE Employee by Name - PASS
@mark.order(15)
@mark.parametrize(
    "tablename, version, name", [param("employees", "v1", "Employee%", id="Employees")]
)
def test_deletename_pass(tablename: str, version: str, name: str):
    response = client.delete(f"/{tablename}/{version}/name/{name}")
    print(f"Endpoint = /{tablename}/{version}/name/{name}")
    assert response.status_code == 202


# DELETE Employee by Name - FAIL
@mark.order(16)
@mark.parametrize(
    "tablename, version, name", [param("employees", "v1", "Employee%", id="Employees")]
)
def test_deletename_fail(tablename: str, version: str, name: str):
    response = client.delete(f"/{tablename}/{version}/name/{name}")
    print(f"Endpoint = /{tablename}/{version}/name/{name}")
    assert response.status_code == 404
