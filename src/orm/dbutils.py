import os
from datetime import datetime

from sqlalchemy.engine.base import Engine
from sqlalchemy_utils import database_exists

from src.helper import applog
from src.orm.dbfunctions import dbBulkInsert
from src.orm.schema import *  # noqa: F403
# from src.orm.schema import Base, Album, Artist, Customer, Currency, Employee, Genre, Invoice, Invoiceitem, Mediatype, Playlist, Playlisttrack, Track
from src.raw.csvhelper import csvDictReader, csvRead


# CREATE database shell
def dbInit(engine: Engine) -> bool:
    """
    CREATE database shell
    :param engine (object): SQLAlchemy engine instance
    :return bool: True or False
    """
    if not database_exists(engine.url):
        Base.metadata.create_all(bind=engine)  # noqa: F405
        applog.info(
            f'Database {engine.url.database} created at {datetime.today().strftime("%d-%m-%Y %H:%M")}'
        )
        return True
    else:
        for t in Base.metadata.sorted_tables:  # noqa: F405
            Base.metadata.create_all(bind=engine, checkfirst=True) # noqa F405
        applog.info(
            f'Database {engine.url} updated at at {datetime.today().strftime("%d-%m-%Y %H:%M")}'
        )
        return True


# RELOAD sample data
def dbFill(session, seed: str, database: str) -> bool:
    """
    RELOAD sample data
    :param session (object): SQLAlchemy session instance
    :param seed (str): Fully qualified CSV file of files to import
    :param database (str): Database name to populate
    :return bool: True or False
    """
    try:
        filesToImport = csvRead(seed)
        if filesToImport is not None:
            for f in enumerate(filesToImport):
                dataToImport = csvDictReader(seed[0 : seed.rfind("/") + 1] + f[1])
                tblName = f[1][0 : f[1].rfind(".")]
                result = dbBulkInsert(session, eval(tblName.title()), dataToImport)
                if result:
                    applog.info(
                        f'Populated {database} {tblName.title()} at {datetime.today().strftime("%d-%m-%Y %H:%M")}'
                    )
            return True
    except Exception as e:
        applog.error(f"{e}")
        return e


# DELETE database
def dbKill(filename: str) -> bool:
    """
    DELETE database
    :param filename (str): Fully qualified path to database name
    :return bool: True or False
    """
    try:
        if os.path.exists(filename):
            os.remove(filename)
            applog.info(
                f'File {filename} has been removed at {datetime.today().strftime("%d-%m-%Y %H:%M")}'
            )

        if not os.path.exists(filename):
            return True
        else:
            applog.warning(f"File {filename} could not be found")
            return False
    except Exception as e:
        return e
