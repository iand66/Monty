import os

from pytest import fixture
from sqlalchemy import text

from src.helper import appcfg, engine, mode, session
from src.orm.dbutils import dbFill, dbInit, dbKill


# Get testing database name
@fixture(scope="session")
def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()


@fixture(scope="session")
def get_count(get_db):
    def _get_count(tablename: str):
        query = f"SELECT COUNT(*) FROM {tablename}"
        result = get_db.execute(text(query))
        count = result.fetchone()[0]
        return count

    return _get_count


# Setup testing environment
@fixture(scope="session")
def dbBuild(get_db):
    """
    dbKill - Delete test database if exists
    dbInit - Create new database shell - orm/schema
    dbFill - Populate new database
    """
    if mode:
        dbname = appcfg.get("DBCFG", "dblive")
    else:
        dbname = appcfg.get("DBCFG", "dbtest")

    if os.path.exists(dbname):
        assert dbKill(dbname) is True
        assert dbInit(engine) is True
    else:
        assert dbInit(engine) is True

    if get_db.bind.name == "sqlite":
        get_db.execute(text("pragma foreign_keys=on"))

    assert dbFill(get_db, "./sam/csv/import.csv", dbname) is True


# Define tmp directory
@fixture(scope="session")
def temp():
    """
    Create tempdir for CSV I/O tests
    """
    if not os.path.exists("./sam/tmp"):
        os.makedirs("./sam/tmp")
    tmpdir = "./sam/tmp"
    return tmpdir
