import logging, os 

from sqlalchemy.engine.base import Engine
from sqlalchemy_utils import database_exists

from src.raw.csvhelper import csvDictReader, csvRead
from src.orm.dbfunctions import dbBulkInsert
from src.orm.schema import *

def dbInit(engine:Engine, echo:bool) -> bool:
    '''
    CREATE database shell
    :param engine - SQLAlchemy engine instance
    :param echo - Enable application logging
    :return boolean - True or False
    '''
    applog = logging.getLogger('AppLog')
    if not database_exists(engine.url):
        Base.metadata.create_all(bind=engine)
        if echo:
            applog.info(f'Database {engine.url.database} created at {datetime.today().strftime("%d-%m-%Y %H:%M")}')
        return True
    else:
        for t in Base.metadata.sorted_tables:
            Base.metadata.create_all(bind=engine, checkfirst=True)
        if echo:
            applog.info(f'Database {engine.url} updated at at {datetime.today().strftime("%d-%m-%Y %H:%M")}')
        return True
    
def dbFill(session, seed:str, database:str, echo:bool, trace:bool) -> bool:
    '''
    RELOAD sample data
    :param engine - SQLAlchemy session instance
    :param seed - Fully qualified CSV file of files to import
    :param database - Database name to populate
    :param echo - Enable application logging
    :param trace - Enable database logging
    :return boolean - True or False
    '''
    applog = logging.getLogger('AppLog')
    try:
        filesToImport = csvRead(seed, echo)
        if filesToImport is not None:
            for f in enumerate(filesToImport):
                dataToImport = csvDictReader(seed[0:seed.rfind('/')+1] + f[1], echo)
                tblName = f[1][0:f[1].rfind('.')-1]
                dbBulkInsert(session, eval(tblName.title()), dataToImport, echo, trace)
                if echo:
                    applog.info(f'{database} {tblName.title()} populated at {datetime.today().strftime("%d-%m-%Y %H:%M")}')
            return True
    except Exception as e:
        if echo:
            applog.error(f'Seed file of sample files could not be found')
        return e

def dbKill(filename:str, echo:bool) -> bool:
    '''
    DELETE database
    :param filename - Fully qualified path to database name
    :param echo - Enable application logging
    :return boolean - True or False
    '''
    applog = logging.getLogger('AppLog')
    try:
        if os.path.exists(filename):
            os.remove(filename)
            if echo:
                applog.info(f'File {filename} has been removed at {datetime.today().strftime("%d-%m-%Y %H:%M")}')
            if not os.path.exists(filename):
                return True
        else:
            if echo:
                applog.warning(f'File {filename} could not be found')
            return False
    except Exception as e:
        return e